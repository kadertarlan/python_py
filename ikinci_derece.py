a=input('x karenin katsayisini girin: ')
b=input('xin katsayisini girin: ')
c=input('sabit terimi girin: ')
delta=b**2-4*a*c
if delta<0:
	print 'reel kok yok'
elif delta==0:
	print 'cakisik iki kok var'
	kok=-b/2*a
	print kok
else:
	print 'iki farkli kok var'
	kok1=(-b+(delta**(1/2)))/2*a
	kok2=(-b-(delta**(1/2)))/2*a
	print kok1, kok2
	print 'Havayi koklayan adam teşekkür eder'
