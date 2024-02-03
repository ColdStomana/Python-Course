username=input()
password=input()
data1=""
while (data1!=password):
    data1=input()

if data1==password:
    print(f"Welcome {username}!")