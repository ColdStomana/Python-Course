cena_ekskurzia=float(input())
broi_pazeli=int(input())
broi_kukli=int(input())
broi_meceta=int(input())
broi_minioni=int(input())
broi_kamioni=int(input())

pazel_cena=2.60
kukla_cena=3
mece_cena=4.10
minion_cena=8.20
kamionce_cena=2

suma=broi_pazeli*pazel_cena+broi_kukli*kukla_cena+broi_meceta*mece_cena+broi_minioni*minion_cena+broi_kamioni*kamionce_cena
broi_igracki=broi_pazeli+broi_kukli+broi_meceta+broi_minioni+broi_kamioni
bonus=0

if broi_igracki>=50:
    bonus=suma*0.25

kraina_cena=suma-bonus
naem=kraina_cena*0.1
pecalba=kraina_cena-naem

if pecalba>=cena_ekskurzia:
    ostavat=pecalba-cena_ekskurzia
    print(f'Yes! {ostavat:.2f} lv left.')
else:
    ostavat=cena_ekskurzia-pecalba
    print(f'Not enough money! {ostavat:.2f} lv needed.')

