nailon = int (input())
boq = int (input())
razreditel = int (input())
casove = int (input())

sumnailon=(nailon +2)*1.50
sumboq=(boq+(0.1*boq))*14.50
sumrazreditel=razreditel*5.00
cenamat=sumnailon+sumboq+sumrazreditel+0.40
cenamaist=cenamat*0.3*casove
totalsum=cenamat+cenamaist

print(totalsum)
