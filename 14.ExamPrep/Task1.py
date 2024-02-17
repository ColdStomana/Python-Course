import math

number_of_people=int(input())
tax=float(input())
price_for_sun_louger=float(input())
umbrella_price=float(input())

total_tax_entrance=number_of_people*tax
sum_lounger_tax=math.ceil(number_of_people*0.75)*price_for_sun_louger
umbrella_tax=math.ceil(number_of_people*0.50)*umbrella_price
total_price=total_tax_entrance+sum_lounger_tax+umbrella_tax
print(f"{total_price:.2f} lv.")
