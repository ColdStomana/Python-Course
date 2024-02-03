number=int(input())
day=input()

if day=="Sunday":
    print("closed")
elif 10<=number<=18:
    print("open")
else:
    print("closed")
