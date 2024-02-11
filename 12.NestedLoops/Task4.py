n=int(input())
m=int(input())
magic_number=int(input())
combination_counter=0
Found_flag=True

for x1 in range(n,m+1):
    for x2 in range (n,m+1):
         combination_counter+=1
         if x1+x2==magic_number and Found_flag:
              print(f"Combination N:{combination_counter} ({x1} + {x2} = {magic_number})")
              Found_flag=False
            

if Found_flag:
 print(f"{combination_counter} combinations - neither equals {magic_number}")
