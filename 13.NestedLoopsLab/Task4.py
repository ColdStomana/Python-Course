num=int(input())
end_flag=True
grade_sum=0
entered_grades=0
mid_sum=0
all_grades=0

while end_flag:
    topic=input()
    if topic=="Finish":
        print(f"Student's final assessment is {all_grades/entered_grades:.2f}.")
        end_flag=False
        break
    grade_sum=0
    for i in range(0,num):
        grade=float(input())
        grade_sum+=grade
        entered_grades+=1
        mid=grade_sum/num
        all_grades+=grade
    print(f"{topic} - {mid:.2f}.")

    