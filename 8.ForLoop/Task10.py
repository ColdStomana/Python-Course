n=int(input())

odd_sum=0
even_sum=0
for i in range(1,n+1):
    number=int(input())
    if i%2==0:
     even_sum+=number
    else:
     odd_sum+=number

if odd_sum==even_sum:
    print(f"Yes")
    print(f"Sum = {odd_sum}")
else:
    diff=abs(odd_sum-even_sum)
    print(f"No")
    print(f"Diff = {diff}")