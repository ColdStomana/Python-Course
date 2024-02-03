import sys

small=sys.maxsize
big=-sys.maxsize

num=int(input())

for i in range (0,num,1):
    num2=int(input())
    if num2<small:
        small=num2
    if num2>big:
        big=num2

print(f"Max number: {big}")
print(f"Min number: {small}")
