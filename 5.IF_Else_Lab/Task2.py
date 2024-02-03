points=float(input())
bonus1=0
bonus2=0
if points <=100:
    bonus1=bonus1+5
elif points>1000:
    bonus1=bonus1+(0.1*points)
elif points>100:
    bonus1=bonus1+(0.2*points)


if (points % 2) == 0:
 bonus2=bonus2+1
elif (points % 10) == 5:
 bonus2=bonus2+2

totalbonus=bonus2+bonus1
print(totalbonus)
print(points+totalbonus)

