budget=float(input())
broi_video=int(input())
broi_procesori=int(input())
broi_ram=int(input())

cena_video=250
total_video=broi_video*cena_video
cena_procesor=0.35*total_video*broi_procesori
cena_ram=0.1*total_video
cena_ram=cena_ram*broi_ram
total_cena=total_video+cena_procesor+cena_ram

if broi_video>broi_procesori:
    total_cena=total_cena-total_cena*0.15

if budget>=total_cena:
    budget=budget-total_cena
    print(f'You have {budget:.2f} leva left!')
else:
    budget=total_cena-budget
    print(f'Not enough money! You need {budget:.2f} leva more!')