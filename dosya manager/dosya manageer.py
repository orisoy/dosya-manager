import os
deney01 = r"C:\Users\Lenovo\OneDrive\Masaüstü\githuba geçecekler\python\dosya manager\dosyalar" #<==== lütfen şuradaki boşluğa "dosyalar" dosyasının yolunu yapıştırınız dikkat tırnka işaretlerine dikkat edin
os.chdir(deney01)

mevcut_dosyalar = os.listdir()

def dosya_oluşturmak():
    isim = str(input("dosya ismi giriniz : ")+".txt")
    yazı = str(input("yazılmka istenen yazıyı giriniz : "))
    dosya = os.open(isim,os.O_RDWR|os.O_CREAT)
    os.write(dosya,yazı.encode())
    print("{} dosyası başarıyla oluşuruldu".format(isim))
    os.close(dosya)

def dosya_içeriği_okumak():
    print(mevcut_dosyalar)
    while True:
        dosya_ismi = input("okunacak dosyanın ismini giriniz : ")+".txt"
        if dosya_ismi in mevcut_dosyalar :
            okunacak_dosya = os.open(dosya_ismi,os.O_RDONLY)
            istatistik = os.stat(okunacak_dosya).st_size
            içerik = os.read(okunacak_dosya,istatistik)
            içerik1 = içerik.decode()
            print("{} dosyasının içeriği : {}".format(dosya_ismi,içerik1))
            break
        print("lütfen listedeki mevcut dosya ismini giriniz")

def dosya_ismi_değiştirmek():
    while True:
        print(mevcut_dosyalar)
        eski_dosya_ismi = input("ismi değişecek dosyanın ismi : ")+".txt"
        if eski_dosya_ismi in mevcut_dosyalar :
            yeni_dosya_ismi = str(input("yeni dosya ismi : ")+".txt")
            os.rename(eski_dosya_ismi,yeni_dosya_ismi)
            print("{} dosya nın adı {} olarak değiştirildi".format(eski_dosya_ismi,yeni_dosya_ismi))
            break
        print("lütfen listedeki mevcut dosya ismini giriniz")
        

def dosya_silmek():
    while True:
        print(mevcut_dosyalar)
        silinecek_dosya = str(input("lütfen silinecek dosya ismini giriniz :")+".txt")
        if silinecek_dosya in mevcut_dosyalar :
            os.remove(silinecek_dosya)
            print("{} başarıyla silindi".format(silinecek_dosya))
            break
    print("lütfen listedeki mevcut dosya ismini giriniz")



print("işlem listesi : lütfen işlemin saysını yazın")


a = 1
while True:
    işlemler= ["dosya_oluşturmak" ,"dosya_içeriği_okumak" ,"dosya_adı_değiştirmek" ,"dosya_silmek"]
    işlemler 
    num = 0
    for a in işlemler:
        num += 1
        print("{} = {}".format(num,a))
    print("[1,2,3,4,x]")
    cvp = str(input("yapmak istediğiniz işlem nedir : "))
    if cvp == "1" :
        dosya_oluşturmak()
    elif cvp == "2" :
        dosya_içeriği_okumak()   
    elif cvp == "3" :
        dosya_ismi_değiştirmek()   
    elif cvp == "4" :
        dosya_silmek()
    elif cvp == "x": 
        print("oturum kapaıldı")
        break
    else: print("geçersiz seçim")
    


















