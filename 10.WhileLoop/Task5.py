inpt=input()
sum=0.0

while inpt!="NoMoreMoney":
    money=float(inpt)
    if money<0:
     print(f"Invalid operation!")
     break

    sum=sum+money
    print(f"Increase: {money:.2f}")
    inpt=input()
print(f"Total: {sum:.2f}")