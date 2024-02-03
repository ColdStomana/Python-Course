import sys

inpt=input()
min=sys.maxsize

while inpt!="Stop":
    current_number=float(inpt)

    if min>current_number:
        min=current_number
    inpt=input()
print(f"{min:.0f}")