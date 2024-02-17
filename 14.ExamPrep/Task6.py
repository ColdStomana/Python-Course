number_of_easter_breads=int(input())
best_baker_name=""
best_baker_score=0

for i in range (number_of_easter_breads):
    baker_name=input()
    current_score=0

    while True:
        command=input()
    
        if command=="Stop":
            print(f"{baker_name} has {current_score} points.")
            break

        points=command
        current_score+=int(points)

    if current_score>best_baker_score:
        best_baker_name=baker_name
        best_baker_score=current_score
        print(f"{best_baker_name} is the new number 1!")

print(f"{best_baker_name} won the competition with {best_baker_score} points!")

