from ultralytics import YOLO
import numpy as np
import sqlite3
import cv2
import multiprocessing
from multiprocessing import Pool

def portlariAl():
    baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
    cursor = baglanti.cursor()
    cursor.execute("SELECT port FROM cameras")
    sonuc = cursor.fetchall()
    if not sonuc:
        baglanti.close()
        return []
    baglanti.close()
    return [r[0] for r in sonuc]

class GoruntuIsleme:
    def __init__(self, portlar):
        self.model = YOLO(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Models\yolov8n.pt")
        self.labels = self.model.names
        self.font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        self.portlar = portlar

    def nesneTanima(self, video):
        # cap = cv2.VideoCapture(self.portlar)
        cap = cv2.VideoCapture(video)

        baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        cursor = baglanti.cursor()
        cursor.execute("SELECT camera_id FROM cameras WHERE port=?", (video,))
        camera_id = cursor.fetchone()[0]

        while True:
            cursor = baglanti.cursor()
            cursor.execute("SELECT * FROM sensors WHERE cameraId=?", (camera_id,))
            sensorler = cursor.fetchall()
            ret, frame = cap.read()
            if not ret:
                break

            sonuc = self.model(frame, verbose=False)
            doldurulmusResim = np.zeros((frame.shape[0], frame.shape[1], 1), dtype=np.uint8)

            for i in range(len(sonuc[0].boxes)):
                x1, y1, x2, y2 = sonuc[0].boxes.xyxy[i]
                skor = sonuc[0].boxes.conf[i]
                label = sonuc[0].boxes.cls[i]

                x1, y1, x2, y2, skor, label = int(x1), int(y1), int(x2), int(y2), float(skor), int(label)
                isim = self.labels[label]
                if skor < 0.5 or isim != 'car':
                    continue

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(doldurulmusResim, (x1, y1), (x2, y2), 255, -1)
                taninan_nesne = isim + str(format(skor, '.2f'))
                cv2.putText(frame, taninan_nesne, (x1, y1 - 5), self.font, 0.8, (255, 0, 0), 2)

            for sensor in sensorler:
                maske = np.zeros((frame.shape[0], frame.shape[1], 1), dtype=np.uint8)
                cv2.rectangle(maske, (sensor[2], sensor[3]), (sensor[8], sensor[9]), 255, -1)
                cv2.rectangle(frame, (sensor[2], sensor[3]), (sensor[8], sensor[9]), (0, 0, 255), -1)
                maske_alani = abs(sensor[8] - sensor[6]) * abs(sensor[9] - sensor[5])
                maske_sonucu = cv2.bitwise_and(doldurulmusResim, maske)
                beyaz_pikseller = np.sum(maske_sonucu == 255)
                sensor_orani = beyaz_pikseller / maske_alani

                if sensor_orani > 0.75 and sensor[10] == 0:
                    cv2.rectangle(frame, (sensor[2], sensor[3]), (sensor[8], sensor[9]), (0, 255, 0), -1)
                    cursor.execute("UPDATE sensors SET situation=? WHERE sensor_id=?", (1, sensor[0]))
                    baglanti.commit()

                elif sensor_orani <= 0.75 and sensor[10] == 1:
                    cv2.rectangle(frame, (sensor[2], sensor[3]), (sensor[8], sensor[9]), (0, 0, 255), -1)
                    cursor.execute("UPDATE sensors SET situation=? WHERE sensor_id=?", (0, sensor[0]))
                    baglanti.commit()

                elif sensor_orani > 0.75 and sensor[10] == 1:
                    cv2.rectangle(frame, (sensor[2], sensor[3]), (sensor[8], sensor[9]), (0, 255, 0), -1)

                else:
                    cv2.rectangle(frame, (sensor[2], sensor[3]), (sensor[8], sensor[9]), (0, 0, 255), -1)

                cv2.putText(frame, str(sensor[1]), (sensor[2] + (sensor[4] - sensor[2]) // 2 - 10, sensor[3] +
                                                    (sensor[7] - sensor[3]) // 2 - 10), self.font, 1,
                            (255, 255, 255), 2)
                cv2.putText(frame, str(sensor[0]), (sensor[2] + (sensor[4] - sensor[2]) // 2 - 5, sensor[3] +
                                                    (sensor[7] - sensor[3]) // 2 + 10), self.font, 1,
                            (255, 255, 255), 2)

            cv2.imshow("Video", frame)

            key = cv2.waitKey(1)
            if key == 27 or cv2.getWindowProperty("Video", cv2.WND_PROP_VISIBLE) < 1:
                break

        baglanti.close()
        cap.release()
        cv2.destroyAllWindows()

    def multiNesneTanima(self):
        processes = []
        for video in self.portlar:
            process = multiprocessing.Process(target=self.nesneTanima, args=(video,))
            processes.append(process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()
