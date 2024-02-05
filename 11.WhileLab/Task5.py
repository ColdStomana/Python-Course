import math
input_sum=float(input())
coin_counter=0
left_coin=input_sum*100

while left_coin!=0:
    if left_coin>=200:
        coin_counter=coin_counter+1
        left_coin=left_coin-200
    elif left_coin>=100:
        coin_counter=coin_counter+1
        left_coin=left_coin-100     
    elif left_coin>=50:
        coin_counter=coin_counter+1
        left_coin=left_coin-50   
    elif left_coin>=20:
        coin_counter=coin_counter+1
        left_coin=left_coin-20
    elif left_coin>=10:
        coin_counter=coin_counter+1
        left_coin=left_coin-10  
    elif left_coin>=5:
        coin_counter=coin_counter+1
        left_coin=left_coin-5
    elif left_coin>=2:
        coin_counter=coin_counter+1
        left_coin=left_coin-2 
    elif left_coin>=1:
        coin_counter=coin_counter+1
        left_coin=left_coin-1  
    left_coin=math.floor(left_coin)

print(coin_counter)


# Float division
#print(10 / 3)  # Output: 3.3333333333333335

# Integer division
#print(10 // 3)  # Output: 3

# Remainder of a division
#print(10 % 3)  # Output: 1