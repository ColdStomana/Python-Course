p1=0
p2=0
p3=0
p4=0
p5=0
total=0
n=int(input())

for i in range (0,n):
    num=int(input())
    total=total+num
    if num<=5:
        p1=p1+num
    elif 6<=num<=12:
        p2=p2+num
    elif 13<=num<=25:
        p3=p3+num
    elif 26<=num<=40:
        p4=p4+num        
    elif num>=41:
        p5=p5+num

p1p=p1/total*100
p2p=p2/total*100
p3p=p3/total*100
p4p=p4/total*100
p5p=p5/total*100

print(f"{p1p:.2f}%")
print(f"{p2p:.2f}%")
print(f"{p3p:.2f}%")
print(f"{p4p:.2f}%")
print(f"{p5p:.2f}%")