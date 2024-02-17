number_of_visitors=int(input())
back, chest, legs, abs_fit, protein_shake, protein_bar = 0, 0, 0, 0, 0, 0

counter_of_Protein_clients=0
counter_of_fitness_clients=0

for i in range (number_of_visitors):
    fitness_activity=input()

    if fitness_activity=="Back":
        back+=1
        counter_of_fitness_clients+=1
    elif fitness_activity=="Chest":
        chest+=1
        counter_of_fitness_clients+=1
    elif fitness_activity=="Legs":
        legs+=1
        counter_of_fitness_clients+=1
    elif fitness_activity=="Abs":
        abs_fit+=1
        counter_of_fitness_clients+=1
    elif fitness_activity=="Protein shake":
        protein_shake+=1
        counter_of_Protein_clients+=1
    elif fitness_activity=="Protein bar":
        protein_bar+=1
        counter_of_Protein_clients+=1

percent_of_trainees=(counter_of_fitness_clients/number_of_visitors)*100
people_come_to_buy_protein=(counter_of_Protein_clients/number_of_visitors)*100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_fit} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percent_of_trainees:.2f}% - work out")
print(f"{people_come_to_buy_protein:.2f}% - protein")