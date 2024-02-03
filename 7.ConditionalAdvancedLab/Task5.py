budget=float(input())
season=input()

where=""
country=""
total_cost=0

if season=="summer":
 where="Camp"
elif season=="winter":
 where="Hotel"

if budget<=100 and season=="summer":
 total_cost=budget*0.3
 country="Bulgaria"
elif budget<=100 and season=="winter":
 total_cost=budget*0.7
 country="Bulgaria"

if 100<budget<=1000 and season=="summer":
 total_cost=budget*0.4
 country="Balkans"
elif 100<budget<=1000 and season=="winter":
 total_cost=budget*0.8
 country="Balkans"
elif budget>1000:
 total_cost=budget*0.9
 country="Europe"
 where="Hotel"

print(f"Somewhere in {country}") 
print(f"{where} - {total_cost:.2f}")