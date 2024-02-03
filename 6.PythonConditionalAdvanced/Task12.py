town=input()
range=float(input())
price=0

valid=town=="Sofia" or town=="Varna" or town=="Plovdiv"
valid_p=range>0

if not valid or not valid_p:
    print("error")


if town=="Sofia":
    if 0<=range<=500:
        price=0.05
    elif 500<range<=1000:
        price=0.07
    if 1000<range<=10000:
        price=0.08
    elif range>10000:
        price=0.12  
elif town=="Varna":
    if 0<=range<=500:
        price=0.045
    elif 500<range<=1000:
        price=0.075
    if 1000<range<=10000:
        price=0.10
    elif range>10000:
        price=0.13  
elif town=="Plovdiv":
    if 0<=range<=500:
        price=0.055
    elif 500<range<=1000:
        price=0.08
    if 1000<range<=10000:
        price=0.12
    elif range>10000:
        price=0.145  

if valid and valid_p:
    total=price*range
    print(f'{total:.2f}')
