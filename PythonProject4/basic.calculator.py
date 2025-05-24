def toplama(sayi1, sayi2):      #islem fonksiyonları
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def bolme(sayi1, sayi2):
    if sayi2 == 0:
        return "işlem geçersiz"
    return sayi1 / sayi2

print("Hesap Makinesine hoş geldiniz!")       #kullanıcıdan sayı ve yapmak istediği işlemi alma

a = int(input("İşlem yapmak istediğiniz ilk sayıyı girin. "))
islem = int(input("yapmak istediğiniz işlemi seçin, toplama-1, cıkarma-2, carpma-3, bolme-4 "))
b = int(input("İşlem yapmak istediğiniz ikinci sayıyı girin. "))


if islem == 1:          #islemler yapılır
   sonuc = toplama(a, b)
elif islem == 2:
    sonuc = cikarma(a, b)
elif islem == 3:
    sonuc = carpma(a, b)
elif islem == 4:
    sonuc = bolme(a, b)
else:
    sonuc = "işlem geçersiz"

print("sonuc. " , sonuc)