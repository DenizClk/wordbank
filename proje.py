import sqlite3
import time
from word import *

print("""***************************** 

Sözlük Programı

İşlemler:

1. Sözlüğü göster

2. Sözcük Sorgulama

3. Sözcük Ekle

4. Çıkış


*****************************""")

sözcük = Sözcükler()


while True:
    choose = input("Lütfen işlem seçiniz: ")

    if (choose=="4"):
        print("Program sonlandırılıyor...")
        print("Unutmayın, hafızayı diri tutmak için sıkı çalışmak şarttır.")
        break

    elif (choose=="1"):
        sözcük.sözlük_göster()


    elif (choose=="2"):
        print("Sözcük sorgulanıyor...")
        time.sleep(2)
        sözcük.sözcük_sorgula()


    elif (choose=="3"):


        sözcük.sözcük_ekle()

    else:
        print("Geçersiz işlem...")






