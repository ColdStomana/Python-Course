type_flowers=input()
num_flowers=int(input())
budget=float(input())

flower_price=0
total_cost=0

if type_flowers=="Roses":
 flower_price=5
elif type_flowers=="Dahlias":
  flower_price=3.80
elif type_flowers=="Tulips":
  flower_price=2.80
elif type_flowers=="Narcissus":
  flower_price=3.
elif type_flowers=="Gladiolus":
  flower_price=2.50

total_cost=flower_price * num_flowers 

if type_flowers=="Roses" and num_flowers > 80:
  total_cost=total_cost-total_cost*0.1
elif type_flowers=="Dahlias" and num_flowers > 90:
  total_cost=total_cost-total_cost*0.15
elif type_flowers=="Tulips" and num_flowers > 80:
  total_cost=total_cost-total_cost*0.15
elif type_flowers=="Narcissus" and num_flowers < 120:
  total_cost=total_cost+total_cost*0.15
elif type_flowers=="Gladiolus" and num_flowers < 80:
  total_cost=total_cost+total_cost*0.2

rest=total_cost-budget
rest1=budget-total_cost

if rest<=0:
  print(f"Hey, you have a great garden with {num_flowers} {type_flowers} and {rest1:.2f} leva left.")
else:
  print(f"Not enough money, you need {rest:.2f} leva more.")