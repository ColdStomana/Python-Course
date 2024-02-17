budget=float(input())
liters_of_fuel=float(input())
day_of_week=input()

fuel_price_per_litre=2.10
tour_guide_price=100

total_fuel_cost=liters_of_fuel*fuel_price_per_litre
total_cost=total_fuel_cost+tour_guide_price

if day_of_week=="Saturday":
    total_cost*=0.9
elif day_of_week=="Sunday":
    total_cost*=0.8


if budget >=total_cost:
    money_left=budget-total_cost
    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_needed=total_cost-budget
    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")