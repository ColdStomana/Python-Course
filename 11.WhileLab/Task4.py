steps_to_make=10000
steps_made=True
total_steps=0

while total_steps<steps_to_make and steps_made==True:
    steps=input()
    if steps=="Going home":
        steps=input()
        n_steps=int(steps)
        total_steps=total_steps+n_steps
        steps_made=False

    if not steps_made==False:
     n_steps=int(steps)
     total_steps=total_steps+n_steps



steps_left= steps_to_make-total_steps
steps_over= total_steps-steps_to_make

if total_steps>=steps_to_make:
    print(f"Goal reached! Good job!")
    print(f"{steps_over} steps over the goal!")
else:
    print(f"{steps_left} more steps to reach goal.")