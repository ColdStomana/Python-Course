group_budget=int(input())
season=input()
fisherman=int(input())

price=0


if season=="Spring":
    price=3000
elif season=="Summer" or season=="Autumn":
    price=4200
elif season=="Winter":
    price=2600

if fisherman <=6 :
    price=price-price*0.1
elif 7 <= fisherman <= 11:
    price=price-price*0.15    
elif fisherman >= 12:
    price=price-price*0.25

if (fisherman%2)==0 and season!="Autumn":
    price=price-price*0.05

rest=price-group_budget
rest1=group_budget-price

if rest<=0:
  print(f"Yes! You have {rest1:.2f} leva left.")
else:
  print(f"Not enough money! You need {rest:.2f} leva.")