needed_profit=float(input())
current_profit=0

TARGET_CONDITION=False
PARTY_CONDITION=False

while True:
    command=input()

    if command=="Party!":
        PARTY_CONDITION=True
        break

    cocktail_name=command
    number_of_cocktails=int(input())
    order_price= len(cocktail_name) * number_of_cocktails

    if order_price %2 !=0:
        order_price-=order_price*0.25

    current_profit+=order_price

    if current_profit>=needed_profit:
        TARGET_CONDITION=True
        break

if PARTY_CONDITION:
    needed_money=needed_profit-current_profit
    print(f"We need {needed_money:.2f} leva more.")
elif TARGET_CONDITION:
    print("Target aquired.")
print(f"Club income - {current_profit:.2f} leva.")