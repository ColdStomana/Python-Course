numhimikali = int (input())
nummarkeri = int (input())
litrapreparat = int (input())
procentnamalenie = int (input())

cenahim=numhimikali*5.80
cenamark=nummarkeri*7.20
cenaprep=litrapreparat*1.20
cena=cenahim+cenamark+cenaprep
procent=procentnamalenie*0.01
cenanamalenie=cena-(cena*procent)

print(cenanamalenie)
