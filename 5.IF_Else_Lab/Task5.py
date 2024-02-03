budget=float(input())
statisti=int(input())
cena_statist=float(input())

suma_dekor=budget*0.1
suma_obleklo=statisti*cena_statist
if statisti >150:
    suma_obleklo=suma_obleklo-suma_obleklo*0.1

total_sum=suma_dekor+suma_obleklo



if total_sum<=budget:
    ostavat=budget-total_sum
    print("Action!")
    print(f'Wingard starts filming with {ostavat:.2f} leva left.')
else:
    ostavat=total_sum-budget
    print("Not enough money!")
    print(f'Wingard needs {ostavat:.2f} leva more.')
