try:
        ilk=int(raw_input('ilk sayiyi girin: '))
        ikinci=int(raw_input('ikinci sayiyi girin: '))
        sonuc = float(ilk) / ikinci
        print sonuc

except ZeroDivisionError:
    print 'sifira bolme tanimli degil'

except ValueError:
    print 'harf degil sayi giriniz'
print '           .......Havayi Koklayan Adam Teþekkür Eder.......'
