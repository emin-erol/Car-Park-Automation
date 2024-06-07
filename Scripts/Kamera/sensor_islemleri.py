from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from Scripts.Otomasyon.yardimUI import SensorleriYonetYardim, SensorSilYardim, SensorGormeYardim
import sabitler as sb
import sqlite3
import cv2

class SensorIslemleri(QWidget):
    def __init__(self, camera_id):
        super().__init__()
        self.camera_id = camera_id
        self.setGeometry(300, 300, 650, 500)
        self.setFixedSize(650, 500)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\sensor.ico"))
        self.setWindowTitle("Sensör Oluştur")
        self.initUI()

    def initUI(self):
        self.ana_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QVBoxLayout()

        self.ana_layout.addLayout(self.top_layout)
        self.ana_layout.addLayout(self.bottom_layout)

        self.yardimButonu = QPushButton()
        self.yardimButonu.setIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"))
        self.yardimButonu.setStyleSheet("border: none; background: transparent;")
        self.yardimButonu.setIconSize(QSize(48, 48))
        self.yardimButonu.clicked.connect(self.yardimPenceresiniAc)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.yardimButonu)
        self.top_layout.addLayout(hbox)

        label_layout = QVBoxLayout()

        pixmap = QPixmap(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\pic.png")
        pixmap = pixmap.scaled(100, 100)
        label = QLabel()
        label.setPixmap(pixmap)
        label_layout.addWidget(label, alignment=Qt.AlignCenter)

        idLabel = QLabel(f"Kamera ID: {self.camera_id}")
        idLabel.setStyleSheet("font-size: 12pt; font-weight: bold;")
        label_layout.addWidget(idLabel, alignment=Qt.AlignCenter)
        self.top_layout.addLayout(label_layout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.top_layout.addWidget(self.scrollArea)

        self.scroll_content = QWidget()
        self.scroll_content_layout = QGridLayout(self.scroll_content)
        self.scrollArea.setWidget(self.scroll_content)

        self.sensor_ekle = QPushButton("Sensör Ekle")
        self.sensor_ekle.setStyleSheet(f"""
                            QPushButton {{
                                font-size: 10pt; 
                                border-radius: 20px; 
                                color: {sb.BUTTON_TEXT_COLOR}; 
                                background-color: {sb.BUTTON_BG_COLOR};
                            }}
                            QPushButton:hover {{
                                background-color: {sb.BUTTON_HOVER_COLOR};
                            }}
                        """)
        self.sensor_ekle.setFixedSize(270, 40)
        self.sensor_ekle.clicked.connect(self.sensorOlustur)

        self.sensor_sil = QPushButton("Sensör Sil")
        self.sensor_sil.setStyleSheet(f"""
                                    QPushButton {{
                                        font-size: 10pt; 
                                        border-radius: 20px; 
                                        color: {sb.BUTTON_TEXT_COLOR}; 
                                        background-color: {sb.BUTTON_BG_COLOR};
                                    }}
                                    QPushButton:hover {{
                                        background-color: {sb.BUTTON_HOVER_COLOR};
                                    }}
                                """)
        self.sensor_sil.setFixedSize(270, 40)
        self.sensor_sil.clicked.connect(self.sensorSil)

        hbox_buttons = QHBoxLayout()
        hbox_buttons.addStretch()
        hbox_buttons.addWidget(self.sensor_ekle)
        hbox_buttons.addWidget(self.sensor_sil)
        hbox_buttons.addStretch()

        self.bottom_layout.addLayout(hbox_buttons)

        self.setLayout(self.ana_layout)

        self.sensorleriGuncelle()

    def sensorleriGuncelle(self):
        self.sensorler = self.sensorBilgileriniAl()

        for i in reversed(range(self.scroll_content_layout.count())):
            widget = self.scroll_content_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        if self.sensorler:
            for i, sensor in enumerate(self.sensorler):
                sensor_label = QLabel(f"{i + 1}. Park Sensörü; ID: {sensor[0]}, "
                                      f"Sol Üst Nokta: ({sensor[2]}, {sensor[3]}), "
                                      f"Sağ Alt Nokta: ({sensor[8]}, {sensor[9]})")
                self.scroll_content_layout.addWidget(sensor_label, i, 0)

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

                    self.sensorleriGuncelle()

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

    def sensorSil(self):
        self.sil = SensorSil()
        self.sil.sensor_silindi.connect(self.sensorleriGuncelle)
        self.sil.show()

    def sensorBilgileriniAl(self):
        baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
        cursor = baglanti.cursor()
        cursor.execute("SELECT * FROM sensors WHERE cameraId=?", (self.camera_id,))
        sensorler = cursor.fetchall()

        return sensorler

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = SensorleriYonetYardim()
        self.yardimPenceresi.show()


class SensorSil(QMainWindow):
    sensor_silindi = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensör Sil")
        self.setGeometry(250, 250, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\sensor.ico"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.baslik = QLabel("Sensör Sil", self)
        self.baslik.setStyleSheet("font-size: 12pt; padding: 10px;")
        self.baslik.setAlignment(Qt.AlignCenter)

        self.idLabel = QLabel("Sensör ID:", self)
        self.idLabel.setStyleSheet("font-size: 10pt;")

        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Sensör Id Giriniz")
        self.idInput.setStyleSheet(f"""
                            font-size: 10pt; 
                            border: 2px solid {sb.BORDER_COLOR};
                            border-radius: 20px; 
                            padding-left: 10px; 
                            color: {sb.TEXT_COLOR}; 
                            background-color: {sb.FRAME_BG_COLOR};
                            ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
                        """)
        self.idInput.setFixedSize(270, 40)

        self.sensor_sil = QPushButton("Sensörü Sil", self)
        self.sensor_sil.setStyleSheet(f"""
                                    QPushButton {{
                                        font-size: 10pt; 
                                        border-radius: 20px; 
                                        color: {sb.BUTTON_TEXT_COLOR}; 
                                        background-color: {sb.BUTTON_BG_COLOR};
                                    }}
                                    QPushButton:hover {{
                                        background-color: {sb.BUTTON_HOVER_COLOR};
                                    }}
                                """)
        self.sensor_sil.setFixedSize(270, 40)
        self.sensor_sil.clicked.connect(self.sensoruSil)

        self.yardimButonu = QPushButton()
        self.yardimButonu.setIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"))
        self.yardimButonu.setStyleSheet("border: none; background: transparent;")
        self.yardimButonu.setIconSize(QSize(48, 48))
        self.yardimButonu.clicked.connect(self.yardimPenceresiniAc)

        formLayout = QVBoxLayout()
        formLayout.addWidget(self.idLabel)
        formLayout.addWidget(self.idInput)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(formLayout)
        hbox.addStretch()

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.sensor_sil)
        buttonLayout.addStretch()

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.baslik)
        verticalLayout.addStretch()
        verticalLayout.addLayout(hbox)
        verticalLayout.addStretch()
        verticalLayout.addLayout(buttonLayout)
        verticalLayout.addStretch()

        mainLayout = QGridLayout()
        mainLayout.addLayout(verticalLayout, 1, 0, 1, 2)
        mainLayout.addWidget(self.yardimButonu, 0, 1, Qt.AlignRight | Qt.AlignTop)

        central_widget.setLayout(mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.sensoruSil()

        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniAc()

    def sensoruSil(self):
        baglanti = None
        cursor = None
        try:
            baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
            cursor = baglanti.cursor()
            sensor_id = self.idInput.text()

            if sensor_id:
                cursor.execute("SELECT * FROM sensors WHERE sensor_id=?", (sensor_id,))
                sonuc = cursor.fetchone()

                if sonuc:
                    cursor.execute("DELETE FROM sensors WHERE sensor_id=?", (sensor_id,))
                    baglanti.commit()
                    onay_mesaji = "Sensör başarıyla silindi."
                    self.idInput.clear()
                    self.sensor_silindi.emit()
                    self.mesajKutusu(onay_mesaji)
                else:
                    hata_mesaji = "Sensör bulunamadı!"
                    self.idInput.clear()
                    self.mesajKutusu(hata_mesaji)
            else:
                hata_mesaji = "Lütfen bir sensör id'si giriniz."
                self.mesajKutusu(hata_mesaji)
        except Exception as e:
            hata_mesaji = "Bir hata oluştu, Hata Kodu: " + e
            self.mesajKutusu(hata_mesaji)
        finally:
            if cursor:
                cursor.close()
            if baglanti:
                baglanti.close()

    def mesajKutusu(self, mesaj):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Bilgi')
        msg_box.setText(f'{mesaj}')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec_()

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = SensorSilYardim()
        self.yardimPenceresi.show()


class SensorleriGor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle("Sensörler")
        self.setGeometry(250, 250, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\sensor.ico"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.baslik = QLabel("Sensörleri Gör", self)
        self.baslik.setStyleSheet("font-size: 12pt; padding: 10px;")
        self.baslik.setAlignment(Qt.AlignCenter)

        self.idLabel = QLabel("Kamera ID:", self)
        self.idLabel.setStyleSheet("font-size: 10pt;")

        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Kameranın ID giriniz")
        self.idInput.setStyleSheet(f"""
                            font-size: 10pt; 
                            border: 2px solid {sb.BORDER_COLOR};
                            border-radius: 20px; 
                            padding-left: 10px; 
                            color: {sb.TEXT_COLOR}; 
                            background-color: {sb.FRAME_BG_COLOR};
                            ::placeholder {{ color: {sb.PLACEHOLDER_COLOR}; }}
                        """)
        self.idInput.setFixedSize(270, 40)

        self.sensorleri_gor_buton = QPushButton("Sensörleri Gör", self)
        self.sensorleri_gor_buton.setStyleSheet(f"""
                                    QPushButton {{
                                        font-size: 10pt; 
                                        border-radius: 20px; 
                                        color: {sb.BUTTON_TEXT_COLOR}; 
                                        background-color: {sb.BUTTON_BG_COLOR};
                                    }}
                                    QPushButton:hover {{
                                        background-color: {sb.BUTTON_HOVER_COLOR};
                                    }}
                                """)
        self.sensorleri_gor_buton.setFixedSize(270, 40)
        self.sensorleri_gor_buton.clicked.connect(self.sensorleriGor)

        self.yardimButonu = QPushButton()
        self.yardimButonu.setIcon(QIcon(r"C:\Users\helpdesk\PycharmProjects\otomasyon\Images\help.ico"))
        self.yardimButonu.setStyleSheet("border: none; background: transparent;")
        self.yardimButonu.setIconSize(QSize(48, 48))
        self.yardimButonu.clicked.connect(self.yardimPenceresiniAc)

        formLayout = QVBoxLayout()
        formLayout.addWidget(self.idLabel)
        formLayout.addWidget(self.idInput)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(formLayout)
        hbox.addStretch()

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.sensorleri_gor_buton)
        buttonLayout.addStretch()

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.baslik)
        verticalLayout.addStretch()
        verticalLayout.addLayout(hbox)
        verticalLayout.addStretch()
        verticalLayout.addLayout(buttonLayout)
        verticalLayout.addStretch()

        mainLayout = QGridLayout()
        mainLayout.addLayout(verticalLayout, 1, 0, 1, 2)
        mainLayout.addWidget(self.yardimButonu, 0, 1, Qt.AlignRight | Qt.AlignTop)

        central_widget.setLayout(mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.sensorleriGor()

        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_F1:
            self.yardimPenceresiniAc()

    def sensorleriGor(self):
        baglanti = None
        cursor = None
        try:
            baglanti = sqlite3.connect(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\user_database.db")
            cursor = baglanti.cursor()
            camera_id = self.idInput.text()

            if camera_id:
                cursor.execute("SELECT * FROM cameras WHERE camera_id=?", (camera_id,))
                sonuc = cursor.fetchone()

                if sonuc:
                    self.close()
                    self.sensorleri_gor = SensorIslemleri(camera_id)
                    self.sensorleri_gor.show()
                else:
                    hata_mesaji = "Kamera bulunamadı!"
                    self.idInput.clear()
                    self.mesajKutusu(hata_mesaji)
            else:
                hata_mesaji = "Lütfen bir Kamera ID'si giriniz."
                self.mesajKutusu(hata_mesaji)
        except Exception as e:
            hata_mesaji = "Bir hata oluştu, Hata Kodu: " + e
            self.mesajKutusu(hata_mesaji)
        finally:
            if cursor:
                cursor.close()
            if baglanti:
                baglanti.close()

    def mesajKutusu(self, mesaj):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Bilgi')
        msg_box.setText(f'{mesaj}')
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec_()

    def yardimPenceresiniAc(self):
        self.yardimPenceresi = SensorGormeYardim()
        self.yardimPenceresi.show()