
#basit bir hesap makinesi

# fonksiyonlar;

def topla(x , y):
    return x + y

def cikar(x , y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y !=0 :
        return x / y 
    else:
        return " Hata"
    

#sayilarin ve islemlerin alinmasi

sayi1 = float(input("Birinci sayiyi giriniz.! :"))
sayi2 = float(input("İkinci sayiyi giriniz.! :"))

print(" Yapmak istediğiniz işlemi seçin")
print("Toplama")
print("Çıkarma")
print("Çarpma")
print("Bölme")

secenek = input ("Seçiminizi yapın (Toplama/Çıkarma/Çarpma/Bölme):")

if secenek=='Toplama':
    print(sayi1 , "+", sayi2 , "=" , topla( sayi1,sayi2 ))
elif secenek=='Çıkarma':
    print(sayi1, "-", sayi2 , '=' , cikar( sayi1 , sayi2))
elif secenek=='Çarpma':
    print(sayi1 , "*", sayi2 , "=" , carp(sayi1 , sayi2))
elif secenek=='Bölme':
    print(sayi1 , "/" , sayi2 , "=" , bol(sayi1 , sayi2))
else : 
    print("Geçersiz giriş")

