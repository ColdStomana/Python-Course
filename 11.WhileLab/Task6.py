import math
cake_lenght=int(input())
cake_width=int(input())
cake=cake_lenght*cake_width

while cake>=0:
    pieces=input()
    if pieces=="STOP":
        break

    people=int(pieces) 

    if cake>=people:
        cake=cake-people
    else:
       break

if cake>people:
 print(f"{cake} pieces are left.")
elif cake<=people:
 cake=people-cake
 print(f"No more cake left! You need {cake} pieces more.")
