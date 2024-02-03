import sys

max_num=-sys.maxsize
sum=0

n=int(input())

for i in range (0,n):
    num=int(input())
    if num>max_num:
        max_num=num
    sum+= num

if max_num==sum-max_num:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    print(f"No")
    sum=sum-max_num
    print(f"Diff = {abs(max_num-sum)}")
