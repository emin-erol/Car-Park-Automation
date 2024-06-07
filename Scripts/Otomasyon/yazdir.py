from datetime import datetime
import win32api
import win32print
import pandas as pd
import sqlite3

def tablolariYazdir():
    tarih = datetime.now().strftime('%d_%m_%Y')
    dosya_adi = f'veriler_{tarih}.xlsx'

    baglanti = sqlite3.connect("user_database.db")

    query = """
                SELECT c.camera_id, c.port, s.t_leftX, s.t_leftY, s.t_rightX, s.t_rightY, 
                        s.b_leftX, s.b_leftY, s.b_rightX, s.b_rightY
                FROM cameras c
                LEFT JOIN sensors s ON c.camera_id = s.cameraId
                """
    df = pd.read_sql_query(query, baglanti)
    df.to_excel(dosya_adi, index=False)

    baglanti.close()

    win32api.ShellExecute(0, "printto", dosya_adi, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)
