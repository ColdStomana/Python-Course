day=int(input())
room=input()
sign=input()

price=0

if room=="room for one person":
 price=18
elif room=="apartment":
 price=25
elif room=="president apartment":
 price=35

day=day-1
total_price=price*day

if day<10 and room=="apartment":
 total_price=total_price-total_price*0.3
elif 10<=day<=15 and room=="apartment":
 total_price=total_price-total_price*0.35
elif day>15 and room=="apartment":
 total_price=total_price-total_price*0.5


if day<10 and room=="president apartment":
 total_price=total_price-total_price*0.10
elif 10>=day<=15 and room=="president apartment":
 total_price=total_price-total_price*0.55
elif day>15 and room=="president apartment":
 total_price=total_price-total_price*0.20

if sign=="positive":
  total_price=total_price+total_price*0.25
elif sign=="negative":
 total_price=total_price-total_price*0.1

print(f"{total_price:.2f}")