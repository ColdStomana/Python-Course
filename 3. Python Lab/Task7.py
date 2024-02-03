fishmenu = int (input())
chickenmenu = int (input())
vegmenu = int (input())

sumfish=fishmenu*10.35
sumchicken=chickenmenu*12.40
sumveg=vegmenu*8.15
totmenu=sumfish+sumchicken+sumveg
desertprice=0.2*totmenu
dostavka=2.50
totalsum=totmenu+desertprice+dostavka

print(totalsum)
