import sys

inpt=input()
max=-sys.maxsize

while inpt!="Stop":
    current_number=float(inpt)

    if max<current_number:
        max=current_number
    inpt=input()
print(f"{max:.0f}")