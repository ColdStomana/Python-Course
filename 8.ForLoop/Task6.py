word=input()

sum=0

for ch in word:
    if ch=="a":
        sum=sum+1
    elif ch=="e":
        sum=sum+2
    elif ch=="i":
        sum=sum+3
    elif ch=="o":
        sum=sum+4
    elif ch=="u":
        sum=sum+5
print(sum)