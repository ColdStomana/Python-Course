name=input()
grades=1.0
sum_grades=0.0
excluded=0

while grades<=12:
    grade=float(input())
    if grade < 4.00:
        excluded=excluded+1
        if excluded>1:
         break   
    if 4 <= grade <= 6:
     sum_grades=sum_grades+grade
     grades=grades+1
    continue

average=sum_grades/12

if excluded==2:
   print (f"{name} has been excluded at {grades:.0f} grade")
else:
   print(f"{name} graduated. Average grade: {average:.2f}")


