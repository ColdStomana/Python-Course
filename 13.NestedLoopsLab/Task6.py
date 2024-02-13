kid_num=0
standart_num=0
student_num=0
kid_num2=0
standart_num2=0
student_num2=0
all_tickets=0
total=0
used_movie=0

end_flag=True
end_flag2=True
full_flag=False

while end_flag:
    inp_name=input()
    if inp_name=="Finish":
        print(f"Total tickets: {all_tickets}")
        if student_num2!=0:
         stud=student_num2*100/all_tickets
        else:
           stud=0
        print(f"{stud:.2f}% student tickets.")
        if standart_num2!=0:
         standart=standart_num2*100/all_tickets
        else:
           standart=0
        print(f"{standart:.2f}% standard tickets.")
        if kid_num2!=0:
         kids=kid_num2*100/all_tickets
        else:
           kids=0
        print(f"{kids:.2f}% kids tickets.")
        end_flag=False
        break

    places=input()
    placesint=int(places)

    while end_flag2:
     if full_flag==False:
          place_type=input()
     if place_type=="End" or full_flag==True:
        used_movie=standart_num+kid_num+student_num
        procent_full=used_movie*100/placesint
        print(f"{inp_name} - {procent_full:.2f}% full.")
        standart_num=0
        student_num=0
        kid_num=0
        total=0
        used_movie=0
        end_flag2=True
        full_flag=False
        break
     if place_type=="standard":
         standart_num+=1
         standart_num2+=1
         all_tickets+=1
         total+=1
     if place_type=="kid":
         kid_num+=1
         kid_num2+=1
         all_tickets+=1
         total+=1
     if place_type=="student":
         student_num+=1
         student_num2+=1
         all_tickets+=1
         total+=1
     if placesint==(total):
         full_flag=True



    