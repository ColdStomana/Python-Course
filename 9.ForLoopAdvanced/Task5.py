tabs=int(input())
salary=float(input())
site=""

for n in range (0,tabs,1):
    site=input()
    if site=="Facebook":
        salary=salary-150
    elif site=="Instagram":
        salary=salary-100
    elif site=="Reddit":
        salary=salary-50


if salary<=0:
     print("You have lost your salary.")
elif salary!=0:
     print(f"{salary:.0f}")