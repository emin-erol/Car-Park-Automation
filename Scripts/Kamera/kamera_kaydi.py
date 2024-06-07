import cv2
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QTimer, Qt

class KameraKaydi(QMainWindow):
    def __init__(self, camera_id):
        super().__init__()
        self.camera_id = camera_id
        self.setWindowTitle(f"{self.camera_id} Kamera Kaydı")
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\security-camera.ico"))
        self.baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("SELECT port FROM cameras WHERE camera_id=?", (self.camera_id,))
        self.port = self.cursor.fetchone()[0]
        self.cap = cv2.VideoCapture(self.port)

        if not self.cap.isOpened():
            QMessageBox.warning(self, "Hata", "Kamera kaydı oynatılamadı.")
            return

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.genislik = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.uzunluk = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.setGeometry(100, 100, self.genislik, self.uzunluk)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(self.genislik, self.uzunluk)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.videoyuOynat)
        self.timer.start(int(1000 / self.fps))

    def videoyuOynat(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            uzunluk, genislik, kanal = frame.shape
            step = kanal * genislik
            q_img = QImage(frame.data, genislik, uzunluk, step, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(q_img))
        else:
            self.cap.release()
            self.timer.stop()
