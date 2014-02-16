# -*- coding:utf-8 -*-
def asal(kaca_kadar):
    if kaca_kadar<2:
        return
    elif kaca_kadar==2:
        print 2
        return
    else:
        print 2
        
        for i in range(3,kaca_kadar):
            bolundu= False
            for j in range(2,i):
                if(i%j==0):
                    bolundu=True
                    break
            if bolundu==False:
                print i

h=int(raw_input("kaça kadar asal sayıları öğrenmek istiyorsunuz:"))
asal(h)

