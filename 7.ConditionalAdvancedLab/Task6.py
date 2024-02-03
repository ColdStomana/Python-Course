N1=int(input())
N2=int(input())
symbol=input()

result=0
odd_even=""

if symbol== "+":
 result=N1+N2
elif symbol== "-":
 result=N1-N2
elif symbol== "*":
 result=N1*N2
elif symbol== "/" and N2 != 0:
 result=N1/N2
elif symbol== "%"and N2 != 0:
 result=N1%N2
else:
 print(f"Cannot divide {N1} by zero")

if result%2==0:
  odd_even="even"
else:
 odd_even="odd"

if symbol== "+" or symbol== "-"  or symbol== "*":
 print(f"{N1} {symbol} {N2} = {result} - {odd_even}")
elif symbol== "/" and N2 != 0:
 print(f"{N1} {symbol} {N2} = {result:.2f}")
elif symbol== "%" and N2 != 0:
 print(f"{N1} {symbol} {N2} = {result}")