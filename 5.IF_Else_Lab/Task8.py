import math
serial=str(input())
episode_lenght=int(input())
rest_lenght=int(input())

launch=rest_lenght*0.125
rest=rest_lenght*0.250

time_left=rest_lenght-launch-rest

needed_time=time_left-episode_lenght
time_needed=episode_lenght-time_left


if time_left>=episode_lenght:
    print(f'You have enough time to watch {serial} and left with {math.ceil(needed_time)} minutes free time.')
else:
    print("You don't have enough time to watch " + f'{serial}, you need {math.ceil(time_needed)} more minutes.')

