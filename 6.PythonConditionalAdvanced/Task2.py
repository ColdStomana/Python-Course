day=input()

valid=day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday" or day=="Saturday" or day=="Sunday"

if not valid:
    print("Error")


if day=="Saturday" or day=="Sunday":
 print("Weekend")
elif day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday":
 print("Working day")