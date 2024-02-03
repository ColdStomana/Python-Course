product=input()
day=input()
quantity=float(input())
price=0

valid=day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday" or day=="Saturday" or day=="Sunday"
valid_p=product=="banana" or product=="apple" or product=="orange" or product=="grapefruit" or product=="kiwi" or product=="pineapple" or product=="grapes"

if not valid or not valid_p:
    print("error")


if day=="Saturday" or day=="Sunday":
    if product=="banana":
        price=2.70
    elif product=="apple":
        price=1.25
    if product=="orange":
        price=0.90
    elif product=="grapefruit":
        price=1.60
    elif product=="kiwi":
        price=3.00
    elif product=="pineapple":
        price=5.60
    elif product=="grapes":
        price=4.20
else:
    if product=="banana":
        price=2.50
    elif product=="apple":
        price=1.20
    if product=="orange":
        price=0.85
    elif product=="grapefruit":
        price=1.45
    elif product=="kiwi":
        price=2.70
    elif product=="pineapple":
        price=5.50
    elif product=="grapes":
        price=3.85

if valid and valid_p:
    total=price*quantity
    print(f'{total:.2f}')
