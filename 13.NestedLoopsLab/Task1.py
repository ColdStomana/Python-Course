num=int(input())
current=1
is_bigger_tnah_n=False

for row in range (1,num+1):
    for col in range (1,row+1):
        if current>num:
            is_bigger_tnah_n=True
            break
        print(str(current)+' ', end='')
        current+=1
    if is_bigger_tnah_n:
        break
    print()
    

