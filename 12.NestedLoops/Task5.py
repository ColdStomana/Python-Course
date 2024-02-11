destination=input()
needed_sum=float(input())
current_sum=0
end_flag=True
dest_flag=True

while end_flag:
    sum=input()
    if sum=="End":
        end_flag=False
        break
    if dest_flag==False:
     destination=str(sum)
     needed_sum=float(input())
     current_sum=0
     sum=0
     dest_flag=True  
    if current_sum<needed_sum:
     sum_int=float(sum) 
     current_sum=current_sum+sum_int
    if current_sum>=needed_sum:
       print(f"Going to {destination}!")
       dest_flag=False

       

        


