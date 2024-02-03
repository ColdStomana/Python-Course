p1=0
p2=0
p3=0
p4=0
p5=0

n=int(input())

for i in range (0,n):
    num=int(input())
    
    if num<200:
        p1+=1
    elif 200<=num<=399:
        p2+=1
    elif 400<=num<=599:
        p3+=1
    elif 600<=num<=799:
        p4+=1        
    elif num>=800:
        p5+=1

p1p=p1/n*100
p2p=p2/n*100
p3p=p3/n*100
p4p=p4/n*100
p5p=p5/n*100

print(f"{p1p:.2f}%")
print(f"{p2p:.2f}%")
print(f"{p3p:.2f}%")
print(f"{p4p:.2f}%")
print(f"{p5p:.2f}%")