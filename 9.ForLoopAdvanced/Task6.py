actor=input()
academy_points=float(input())
reviewers_num=int(input())
reviewer=""
points=0
total_points=0

for n in range(0,reviewers_num,1):
    reviewer=input()
    reviewer_point=float(input())
    points=len(reviewer)
    academy_points=academy_points+((reviewer_point*points)/2)

    if academy_points>=1250.5:
     print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")
     break

if academy_points<=1250.5:
     M=1250.5-academy_points
     print(f"Sorry, {actor} you need {M:.1f} more!")
