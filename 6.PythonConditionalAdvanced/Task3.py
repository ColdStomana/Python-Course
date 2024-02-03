day=input()

valid=day=="dog" or day=="crocodile" or day=="tortoise" or day=="snake"

if not valid:
    print("unknown")


if day=="dog":
 print("mammal")
elif day=="crocodile" or day=="tortoise" or day=="snake":
 print("reptile")