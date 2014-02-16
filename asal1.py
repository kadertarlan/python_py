# -*- coding:utf-8 -*-

def asal(kaca_kadar):
    """Asal sayı bulan fonksiyon
    Girdi olarak bir sayı alır
    Bu sayıya kadar olan asal sayıları ekrana basar.
    """
    asallar = [2]
    if kaca_kadar < 2:
        return None
    elif kaca_kadar == 2:
        return asallar
    else:
        for i in range(3,kaca_kadar):
            bolundu = False
            for j in range(2,i):
                if i % j == 0:
                    bolundu=True
                    break
            if bolundu == False:
                asallar.append(i)
    return asallar
    
if __name__ == "__main__":
    # join kullanmak için, listedekiler str olmalı.
    print "\n".join(map(str,asal(1000)))
    """
    Bu aşamada map() bilinmiyorsa, list comprehension veya for döngüsü kullanılır.
    print "\n".join([str(asal) for asal in asal(1000)])
    for asal in asal(1000)
        print asal
    """
