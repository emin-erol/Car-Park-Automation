from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from Scripts.Otomasyon.yardimUI import SensorleriYonetYardim
import sqlite3
import cv2


class SensorIslemleri(QWidget):
    def __init__(self, camera_id):
        super().__init__()
        self.camera_id = camera_id
        self.setGeometry(300, 300, 400, 400)
        self.setFixedSize(400, 400)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\sensor.ico"))
        self.setWindowTitle("Sensör Oluştur")
        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        vbox = QVBoxLayout()
        pixmap = QPixmap(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\pic.png")
        pixmap = pixmap.scaled(100, 100)
        label = QLabel()
        label.setPixmap(pixmap)

        self.idLabel = QLabel(f"Kamera ID: {self.camera_id}")
        self.idLabel.setStyleSheet("font-size: 12pt; font-wight: bold;")
        self.sensorler, self.sensor_sayisi = self.sensorBilgileriniAl()

        self.sensor1 = QLabel()
        self.sensor2 = QLabel()
        self.sensor3 = QLabel()
        self.sensor1.setText(f"1. Park Sensörü: {self.sensorler[0]}")
        self.sensor2.setText(f"2. Park Sensörü: {self.sensorler[1]}")
        self.sensor3.setText(f"3. Park Sensörü: {self.sensorler[2]}")

        self.sensorEkleButton = QPushButton("Sensör Ekle")
        self.sensorEkleButton.clicked.connect(self.sensorOlustur)
        self.sensorEkleButton.hide()

        self.limitLabel = QLabel("Tüm park alanları yapılandırıldı!")
        self.limitLabel.hide()

        self.yardimButonu = QPushButton()
        self.yardimButonu.setIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"))
        self.yardimButonu.setStyleSheet("border: none; background: transparent;")
        self.yardimButonu.setIconSize(QSize(48, 48))
        self.yardimButonu.clicked.connect(self.yardimPenceresiniAc)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.yardimButonu)
        self.vbox.addLayout(hbox)

        if self.sensor_sayisi < 3:
            self.sensorEkleButton.show()
        else:
            self.limitLabel.show()

        self.vbox.addStretch()
        self.vbox.addWidget(label, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vbox.addStretch()
        self.vbox.addWidget(self.idLabel, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vbox.addStretch()
        self.vbox.addWidget(self.sensor1, alignment=Qt.AlignCenter | Qt.AlignVCenter)
        self.vbox.addWidget(self.sensor2, alignment=Qt.AlignCenter | Qt.AlignVCenter)
        self.vbox.addWidget(self.sensor3, alignment=Qt.AlignCenter | Qt.AlignVCenter)
        self.vbox.addStretch()
        self.vbox.addWidget(self.sensorEkleButton, alignment=Qt.AlignCenter | Qt.AlignVCenter)
        self.vbox.addWidget(self.limitLabel, alignment=Qt.AlignCenter | Qt.AlignVCenter)
        self.vbox.addStretch()

        self.hbox.addLayout(self.vbox)

        self.setLayout(self.hbox)

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.frame, (x, y), 3, (0, 255, 0), 1)
            self.noktalar.append((x, y))
            self.noktalar_index += 1
            cv2.imshow('Kamera', self.frame)  # Burayi silerek tekrar dene

            if self.noktalar_index == 2:
                self.noktalar = sorted(self.noktalar, key=lambda x: x[0])
                t_left = self.noktalar[0]  # sol ust kose
                b_right = self.noktalar[1]  # sag alt kose
                t_right = (b_right[0], t_left[1])  # sag ust kose
                b_left = (t_left[0], b_right[1])  # sol alt kose

                cv2.rectangle(self.frame, t_left, b_right, (255, 0, 0), 2)

                # dort noktanin koordinatlarinin ekrana yazdirilmasi
                for i, (x, y) in enumerate([t_left, t_right, b_right, b_left], 1):
                    if i < 3:
                        cv2.putText(self.frame, f"{i}: ({x}, {y})", (x - 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.4,
                                    (0, 255, 0), 1)
                    else:
                        cv2.putText(self.frame, f"{i}: ({x}, {y})", (x - 20, y + 20), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.4,
                                    (0, 255, 0), 1)

                cv2.imshow('Kamera', self.frame)
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Question)
                msg_box.setText("Oluşturulan sensör kaydedilecek, onaylıyor musunuz?")
                msg_box.setWindowTitle("Kontrol")
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                secim_sonucu = msg_box.exec_()
                if secim_sonucu == QMessageBox.Yes:
                    baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
                    cursor = baglanti.cursor()
                    cursor.execute('''INSERT INTO sensors (cameraId, t_leftX, t_leftY, t_rightX,
                                                        t_rightY, b_leftX, b_leftY, b_rightX, b_rightY, situation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (self.camera_id, t_left[0], t_left[1], t_right[0],
                                    t_right[1], b_left[0], b_left[1], b_right[0],
                                    b_right[1], 0))

                    baglanti.commit()
                    baglanti.close()

                    self.sensorler, self.sensor_sayisi = self.sensorBilgileriniAl()
                    self.sensor1.setText(f"1. Park Sensörü: {self.sensorler[0]}")
                    self.sensor2.setText(f"2. Park Sensörü: {self.sensorler[1]}")
                    self.sensor3.setText(f"3. Park Sensörü: {self.sensorler[2]}")

                    if self.sensor_sayisi < 3:
                        self.limitLabel.hide()
                        self.sensorEkleButton.show()
                    else:
                        self.sensorEkleButton.hide()
                        self.limitLabel.show()

                    cv2.destroyAllWindows()
                else:
                    cv2.destroyAllWindows()

    def sensorOlustur(self):
        baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        cursor = baglanti.cursor()
        cursor.execute("SELECT port FROM cameras WHERE camera_id=?", (self.camera_id,))
        port = cursor.fetchone()[0]

        cap = cv2.VideoCapture(port)
        _, self.frame = cap.read()
        cap.release()
        self.noktalar = []
        self.noktalar_index = 0

        cv2.imshow('Kamera', self.frame)
        cv2.setMouseCallback('Kamera', self.click_event)

    def sensorBilgileriniAl(self):
        sensor_sayisi = 0
        baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        cursor = baglanti.cursor()
        cursor.execute("SELECT * FROM sensors WHERE cameraId=?", (self.camera_id,))
        veriler = cursor.fetchall()

        try:
            sensor1 = veriler[0]
            sensor_sayisi += 1
        except:
            sensor1 = "Veri Yok"
        try:
            sensor2 = veriler[1]
            sensor_sayisi += 1
        except:
            sensor2 = "Veri Yok"
        try:
            sensor3 = veriler[2]
            sensor_sayisi += 1
        except:
            sensor3 = "Veri Yok"

        sensorler = [sensor1, sensor2, sensor3]

        return sensorler, sensor_sayisi

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = SensorleriYonetYardim()
        self.yardimPenceresi.show()
