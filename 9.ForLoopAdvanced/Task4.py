age_lili=int(input())
washer_price=float(input())
toy_price=float(input())

toys_num=0
received_money=0
ten=0
took=0

for age in range(1,age_lili+1,1):
    if age%2==0:
        received_money=received_money+10+ten
        ten=ten+10
        took=took+1
    else:
        toys_num=toys_num+1

total_money=received_money+(toy_price*toys_num)-took

if washer_price<=total_money:
 N=total_money-washer_price
 print(f"Yes! {N:.2f}") 
else:
 M=washer_price-total_money
 print(f"No! {M:.2f}") 