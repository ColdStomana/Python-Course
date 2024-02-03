import math
n=int(input())
all_points=int(input())
initial_points=all_points
win=0

for i in range (0,n):
    tournamnet=input()
    if tournamnet=="F":
        all_points=all_points+1200
    elif tournamnet=="SF":
        all_points=all_points+720
    elif tournamnet=="W":
        all_points=all_points+2000
        win=win+1

average_points=all_points-initial_points
average_points=math.floor(average_points/n)
average_win=(win/n)*100

print(f"Final points: {all_points:.0f}")
print(f"Average points: {average_points:.0f}")
print(f"{average_win:.2f}%")