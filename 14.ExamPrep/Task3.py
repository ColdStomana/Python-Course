name_of_city=input()
type_of_pack=input()
vip_pass=input()
days_of_stay=int(input())

number_of_nights= days_of_stay-1 if days_of_stay>7 else days_of_stay
costs=0

INVALID_INPUT=False
NEGATIVE_NUMBER=False

if days_of_stay<=0:
    NEGATIVE_NUMBER=True
else:
    if name_of_city in ("Bansko","Borovets"):
        if type_of_pack=="noEquipment":
            current_cost= 80 * number_of_nights
            costs=current_cost-(current_cost*0.05) if vip_pass=="yes" else current_cost

        elif type_of_pack=="withEquipment":
            current_cost= 100 * number_of_nights
            costs=current_cost-(current_cost*0.10) if vip_pass=="yes" else current_cost

        else:
            INVALID_INPUT=True

    elif name_of_city in ("Varna","Burgas"):
        if type_of_pack=="noBreakfast":
            current_cost= 100 * number_of_nights
            costs=current_cost-(current_cost*0.07) if vip_pass=="yes" else current_cost

        elif type_of_pack=="withBreakfast":
            current_cost= 130 * number_of_nights
            costs=current_cost-(current_cost*0.12) if vip_pass=="yes" else current_cost

        else:
            INVALID_INPUT=True

    else:
        INVALID_INPUT=True

if NEGATIVE_NUMBER:
    print("Days must be positive number!")
elif INVALID_INPUT:
    print("Invalid input!")
else:
    print(f"The price is {costs:.2f}lv! Have a nice time!")
