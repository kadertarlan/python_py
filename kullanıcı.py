a = 1

kullanici_adi = "hakan"
parola = "havayikoklayanadam"

while a == 1:
    kull_ad = raw_input("Kullan�c� ad�: ")
    par = raw_input("Parola: ")
    
    if kull_ad == kullanici_adi and par == parola:
        print "Programa hosgeldiniz!"
        a = 2
    elif not kull_ad or not par:
        print "Bu alanlar� bos b�rakamazs�n�z!"
    else:
        print "Kullan�c� ad� veya parolan�z hatal�."
