month=input()
num_days=int(input())

rent_studio=0
rent_appartment=0

if month=="May" or month=="October":
    rent_studio=50
    rent_appartment=65
elif month=="June" or month=="September":
    rent_studio=75.20
    rent_appartment=68.70
elif month=="July" or month=="August":
    rent_studio=76
    rent_appartment=77

total_apart=rent_appartment*num_days
total_studio=rent_studio*num_days

if 14>num_days >7 and (month=="May" or month=="October"):
 total_studio=total_studio-total_studio*0.05
elif num_days >14 and (month=="May" or month=="October"):
 total_studio=total_studio-total_studio*0.3
elif num_days >14 and (month=="June" or month=="September"):
 total_studio=total_studio-total_studio*0.2

if num_days >14:
    total_apart=total_apart-total_apart*0.1


print(f"Apartment: {total_apart:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")