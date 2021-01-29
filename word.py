import sqlite3
import time

class Sözcük():
    def __init__(self,sözcük,anlamı):
        self.sözcük=sözcük
        self.anlamı=anlamı

    def __str__(self):
        return "Sözcük: {}\nAnlamı{}\n".format(self.sözcük,self.anlamı)

class Sözcükler():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("customer.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "create table if not exists customers (sözcük TEXT,anlamı TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def sözlük_göster(self):
        sorgu = "select * from customers"
        self.cursor.execute(sorgu)
        sözcükler = self.cursor.fetchall()
        
        if (len(sözcükler)==0):
            print("Herhangi bir veriye rastlanılmadı...")

        else:
            for i in sözcükler:
                print(i[0] + ":" + i[1])

    def sözcük_sorgula(self):
        sözcük = input("Sözcük giriniz: ").lower()
        sorgu = "select * from customers"
        anlam =self.cursor.execute(sorgu)
        for i in anlam:
            if (i[0]==sözcük):
                print(sözcük + "\t:"+ i[1])


    def sözcük_ekle(self):

        self.sözcük = input("İngilizce sözcük giriniz: ").lower()
        self.anlamı = input("Türkçesini giriniz: ").lower()
        self.cursor.execute("insert into customers values (?,?)",(self.sözcük,self.anlamı))
        self.baglanti.commit()
        print("Sözcük veritabanına başarıyla eklendi")





