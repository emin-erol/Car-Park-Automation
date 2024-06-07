from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class NasilKullanilirYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yardım')
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        ana_baslik = QLabel("OTOPARK OTOMASYONU NASIL KULLANILIR")
        ana_baslik.setStyleSheet("font-weight: bold; font-size: 24px;")
        layout.addWidget(ana_baslik)

        ana_icerik = QLabel("- Uygulama, otoparktaki güvenlik kameralarından aldığı verileri kullanarak araç tanıma"
                            " işlemi yapan, yine güvenlik kameralarından aldığı verileri kullanarak park alanlarının"
                            " belirlenip sensörler yerleştirilmesini sağlayan, daha sonra tanınan araçların sensörlerle"
                            " ilişkisini hesaplayıp elde edilen bilgilerin veri tabanına geçirilmesini ve her an güncel"
                            " bilgilerin anasayfada gösterilmesini sağlar.")
        ana_icerik.setStyleSheet("font-size: 16px;")
        ana_icerik.setWordWrap(True)
        layout.addWidget(ana_icerik)

        baslik1 = QLabel("1. Kameraların Eklenmesi")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- Uygulamanın kullanılabilmesi için öncelikle Kameraları düzenleyen uygulama açılmalıdır." 
            " Açılan uygulamada gerekli yönlendirmeler takip edilerek kameralar sisteme dahil edilir ve her kameranın"
            " görüntü verileri kullanılarak park alanlarına sensörler yerleştirilir. Kameraların ve sensörlerinin"
            " kayıtlarını bastırmak için menüden Yazdır seçeneği kullanılabilir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        baslik2 = QLabel("1.1. Park Alanlarının Takibi")
        baslik2.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik2)

        icerik2 = QLabel("- Kameralar ve sensörleri programa eklendikten sonra Otomasyon uygulaması açılır. Bu uygulamada"
                         " eklenen sensörlerin durumunu gösteren kutucuklar bulunur. Bunlar ilgili oldukları park"
                         " alanlarına dair bilgiler içerir. Kırmızı kutucuklar dolu park alanlarını temsil ederken"
                         " yeşil kutucuklar henüz dolmamış park alanlarını temsil eder.")
        icerik2.setStyleSheet("font-size: 16px;")
        icerik2.setWordWrap(True)
        layout.addWidget(icerik2)

        self.setLayout(layout)


class AnasayfaYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yardım')
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        ana_baslik = QLabel("OTOPARK OTOMASYONU")
        ana_baslik.setStyleSheet("font-weight: bold; font-size: 24px;")
        layout.addWidget(ana_baslik)

        ana_icerik = QLabel("- Uygulama, otoparktaki güvenlik kameralarından aldığı verileri kullanarak araç tanıma"
                            " işlemi yapan, yine güvenlik kameralarından aldığı verileri kullanarak park alanlarının"
                            " belirlenip sensörler yerleştirilmesini sağlayan, daha sonra tanınan araçların sensörlerle"
                            " ilişkisini hesaplayıp elde edilen bilgilerin veri tabanına geçirilmesini ve her an güncel"
                            " bilgilerin anasayfada gösterilmesini sağlar.")
        ana_icerik.setStyleSheet("font-size: 16px;")
        ana_icerik.setWordWrap(True)
        layout.addWidget(ana_icerik)

        baslik1 = QLabel("1. Anasayfa")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- Bu pencere, uygulamanın anasayfasıdır ve park alanlarının doluluk durumu gösterilmektedir." 
            "Ekranda gözüken kutular park alanlarını temsil etmektedir. Kırmızı renkli kutu, dolu park alanını;"
            "yeşil renkli kutu ise boş park alanını temsil etmektedir. Park alanlarını temsil eden kutuların"
            "altında ilgili park alanını kontrol eden sensörün benzersiz kimlik (id) bilgisi bulunmaktadır."
            "Bu kimlik bilgisi ile ilgili kutunun hangi kamera ve sensöre ait olduğu belirli olacaktır. Gerektiği"
            "zaman kontrol edilmesi sağlanabilmektedir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        baslik2 = QLabel("1.1. Park Alanları")
        baslik2.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik2)

        icerik2 = QLabel("- Bu arayüzde park alanlarının doluluk durumu gösterilmektedir. Ekranda gözüken kutular"
                         " park alanlarını temsil etmektedir. Kırmızı renkli kutu, boş park alanını; yeşil renkli"
                         " kutu ise dolu park alanını temsil etmektedir. Park alanlarını temsil eden kutuların"
                         " altında ilgili park alanını kontrol eden sensörün benzersiz kimlik (id) bilgisi bulunmaktadır.")
        icerik2.setStyleSheet("font-size: 16px;")
        icerik2.setWordWrap(True)
        layout.addWidget(icerik2)

        baslik3 = QLabel("1.2. Park Sensörlerinin Çalışması")
        baslik3.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik3)

        icerik3 = QLabel("- Kameralar sisteme bağlandıktan sonra her kameranın gördüğü park alanlarına sanal sensörler"
                         " yerleştirilir. Bu sensörler bağlı oldukları park alanında bir araç olup olmadığını kontrol"
                         " eder. Aracın bulunduğu bölgeyi kaplayan en küçük dikdörtgen alan (kontur) sensöre yeterli"
                         " miktarda yerleştiğinde sensör aktif duruma gelir ve park alanının dolduğu bilgisini döndürür.")
        icerik3.setStyleSheet("font-size: 16px;")
        icerik3.setWordWrap(True)
        layout.addWidget(icerik3)

        self.setLayout(layout)


class KameralarYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yardım')
        self.setGeometry(100, 100, 850, 650)
        self.setFixedSize(850, 650)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        ana_baslik = QLabel("ARKA PLAN OTOMASYONU")
        ana_baslik.setStyleSheet("font-weight: bold; font-size: 24px;")
        layout.addWidget(ana_baslik)

        ana_icerik = QLabel("- Otomasyon, esasında otoparka yerleştirilen fiziksel güvenlik kameralarını kullanmayı sağlar"
                            " Park alanlarının tespit edilmesi ve doluluk durumunun kontrol edilebilmesi için öncelikle"
                            " park alanlarını gören kameraların görüntü verilerine ulaşmak gerekir bunun için bu otomasyon"
                            " kullanıcının kameraları sisteme tanıtmasını sağlar. Eklenen kameralardaki görüntüler"
                            " kullanılarak park alanlarına sensörlerin yerleştirilmesini de kapsar.")
        ana_icerik.setStyleSheet("font-size: 16px;")
        ana_icerik.setWordWrap(True)
        layout.addWidget(ana_icerik)

        baslik1 = QLabel("1. Kamera İşlemleri")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- İki tür kamera işlemi vardır; bunlar kamera ekleme ve kamera silme işlemleridir. Pencerenin"
                         " sol alt köşesine yerleştirilmiş butonlar aracılığıyla yeni kameraların eklenmesi veya var olan"
                         " kameraların silinmesini sağlar. Kullanılmayan veya hatalı çalışan kameraların sistemden silinmesi"
                         " ve alana yeni eklenen güvenlik kamerasının sisteme dahil edilmesi önemlidir."
                         " Bu kimlik bilgisi ile ilgili kutunun hangi kamera ve sensöre ait olduğu belirli olacaktır. Gerektiği "
                         " vakit kontrol edilmesi sağlanabilmektedir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        baslik2 = QLabel("1.1. Kamera Ekleme")
        baslik2.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik2)

        icerik2 = QLabel("- Pencerenin sol alt köşesinde bulunan 'Kamera Ekle' butonuna basıldığında kamera ekleme"
                         " penceresi açılır. Bu pencerede kullanıcıdan iki adet veri girişi beklenir. Bunlar kameranın"
                         " adını ve port bilgisini oluşturur. Ad bilgisi gerektiği yerde kameraya erişim sağlanabilmesi"
                         " ve ilgili kaydın hangi kameraya ait olduğunu bulmak amacıyla gereklidir. Port bilgisi ise"
                         "güvenlik kamerasının verilerine erişmek için gereklidir. Güvenlik kamerası, verilerini hangi"
                         "adreste tutuyorsa o bilgi buraya girilmelidir. Aksi taktirde kamera kayıtlarına erişim sağlanamaz."
                         "Bu iki bilgi girildikten sonra altında bulunan ekleme butonuna basıldığında kamera ekleme işlemi"
                         "gerçekleşecektir.")
        icerik2.setStyleSheet("font-size: 16px;")
        icerik2.setWordWrap(True)
        layout.addWidget(icerik2)

        baslik3 = QLabel("1.2. Kamera Silme")
        baslik3.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik3)

        icerik3 = QLabel("- Pencerenin sol alt köşesinde bulunan 'Kamera Silme' butonuna basıldığında kamera silme"
                         " penceresi açılır. Bu pencerede, kullanıcıdan silinmesini istediği kameranın adını girmesi"
                         " beklenir. Kullanıcı, silmek istediği kameranın adını girdikten sonra altında bulunan silme"
                         " butonuna bastığında kamera silme işlemi gerçekleştirilir.")
        icerik3.setStyleSheet("font-size: 16px;")
        icerik3.setWordWrap(True)
        layout.addWidget(icerik3)

        baslik4 = QLabel("1.3. Ekranı Yenileme")
        baslik4.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik4)

        icerik4 = QLabel("- Yine pencerenin sol alt köşesinde bulunan 'Yenile' butonu, bu arayüzün yenilenmesini sağlar."
                         " bu sayede güncel veriler ekranda gösterilir. Kamera ekleme veya silme işlemlerinden sonra"
                         " mutlaka yenileme işlemi uygulanmalıdır aksi taktirde güncel veriler ekranda gösterilemez.")
        icerik4.setStyleSheet("font-size: 16px;")
        icerik4.setWordWrap(True)
        layout.addWidget(icerik4)

        self.setLayout(layout)


class KameraEkleYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Ekleme İşlemi")
        self.setGeometry(300, 300, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        baslik1 = QLabel("1. Kamera Ekleme")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel(" Bu pencerede kullanıcıdan iki adet veri girişi beklenir. Bunlar kameranın adını ve port"
                         " bilgisini oluşturur. Ad bilgisi gerektiği yerde kameraya erişim sağlanabilmesi ve ilgili"
                         " kaydın hangi kameraya ait olduğunu bulmak amacıyla gereklidir. Port bilgisi ise güvenlik"
                         " kamerasının verilerine erişmek için gereklidir. Güvenlik kamerası, verilerini hangi adreste"
                         " tutuyorsa o bilgi buraya girilmelidir. Aksi taktirde kamera kayıtlarına erişim sağlanamaz."
                         " Bu iki bilgi girildikten sonra altında bulunan ekleme butonuna basıldığında kamera ekleme "
                         " işlemi gerçekleşecektir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        self.setLayout(layout)


class KameraSilYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Silme İşlemi")
        self.setGeometry(300, 300, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        baslik1 = QLabel("1. Kamera Silme")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- Pencerenin sol alt köşesinde bulunan 'Kamera Silme' butonuna basıldığında kamera silme"
                         " penceresi açılır. Bu pencerede, kullanıcıdan silinmesini istediği kameranın adını girmesi"
                         " beklenir. Kullanıcı, silmek istediği kameranın adını girdikten sonra altında bulunan silme"
                         " butonuna bastığında kamera silme işlemi gerçekleştirilir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        self.setLayout(layout)


class SensorleriYonetYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Silme İşlemi")
        self.setGeometry(400, 400, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        baslik1 = QLabel("1. Sensör İşlemleri")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- Sisteme kaydedilen her kamera üç adet park alanı görecek şekilde tasarlanmıştır. Bu nedenle"
                         " üç adet park alanına sensörlerin yerleştirilmesi bu pencerede gerçekleştirilir. Pencerede "
                         " kameraya ait sensörlerin listesi gösterilmektedir. Tanımlanmamış sensörler için 'Veri Yok'"
                         " ibaresi yer almaktadır. Aşağıda bulunan 'Sensör Ekle' butonuna tıkladıktan sonra kameradan"
                         " bir görüntü alınır ve burada kullanıcının iki nokta seçerek park alanını oluşturması,"
                         " ardından gelen uyarı penceresine onayı vermesi beklenir. Bu işlem sonunda sensör, başarıyla"
                         " kameraya eklenir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        self.setLayout(layout)


class KameraAcYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Açma İşlemi")
        self.setGeometry(300, 300, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        baslik1 = QLabel("1. Kamera Açma")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- Pencerenin sol alt köşesinde bulunan 'Kamera Silme' butonuna basıldığında kamera silme"
                         " penceresi açılır. Bu pencerede, kullanıcıdan silinmesini istediği kameranın adını girmesi"
                         " beklenir. Kullanıcı, silmek istediği kameranın adını girdikten sonra altında bulunan silme"
                         " butonuna bastığında kamera silme işlemi gerçekleştirilir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        self.setLayout(layout)


class SensorSilYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensör Silme İşlemi")
        self.setGeometry(300, 300, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        baslik1 = QLabel("1. Sensör Silme")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- Pencerenin sol alt köşesinde bulunan 'Kamera Silme' butonuna basıldığında kamera silme"
                         " penceresi açılır. Bu pencerede, kullanıcıdan silinmesini istediği kameranın adını girmesi"
                         " beklenir. Kullanıcı, silmek istediği kameranın adını girdikten sonra altında bulunan silme"
                         " butonuna bastığında kamera silme işlemi gerçekleştirilir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        self.setLayout(layout)


class SensorGormeYardim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensörleri Görme İşlemi")
        self.setGeometry(300, 300, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon(r"C:\Users\helpdesk\Desktop\Kamera Otomasyonu\Images\help.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        baslik1 = QLabel("1. Sensör Ekleme")
        baslik1.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(baslik1)

        icerik1 = QLabel("- Pencerenin sol alt köşesinde bulunan 'Kamera Silme' butonuna basıldığında kamera silme"
                         " penceresi açılır. Bu pencerede, kullanıcıdan silinmesini istediği kameranın adını girmesi"
                         " beklenir. Kullanıcı, silmek istediği kameranın adını girdikten sonra altında bulunan silme"
                         " butonuna bastığında kamera silme işlemi gerçekleştirilir.")
        icerik1.setStyleSheet("font-size: 16px;")
        icerik1.setWordWrap(True)
        layout.addWidget(icerik1)

        self.setLayout(layout)

