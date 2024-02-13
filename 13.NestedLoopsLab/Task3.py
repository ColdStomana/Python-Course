prime_sum=0
no_prime_sum=0
end_flag=True
flag=False

while end_flag:
    sum=input()
    if sum=="stop":
        end_flag=False
        break
    sum_num=int(sum)
    if sum_num<0:
       print("Number is negative.")
       continue
    for i in range(2, sum_num):
        if (sum_num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
    if flag==False:
        prime_sum+=sum_num
    if flag==True:
        no_prime_sum+=sum_num
        flag=False

print(f"Sum of all prime numbers is: {prime_sum}") 
print(f"Sum of all non prime numbers is: {no_prime_sum}")
        


