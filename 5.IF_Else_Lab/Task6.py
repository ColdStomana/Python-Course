import math
record_secundi=float(input())
rastoqnie=float(input())
vreme=float(input())

vreme_ivan=rastoqnie*vreme
zakasnenie=(rastoqnie//15)*12.5
total_time=zakasnenie+vreme_ivan

if total_time<record_secundi:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    time_left=total_time-record_secundi
    print(f'No, he failed! He was {time_left:.2f} seconds slower.')