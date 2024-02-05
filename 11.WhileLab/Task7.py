lenght=int(input())
width=int(input())
height=int(input())

room=height*width*lenght
total_room=room
baggage=0

while room>0:
    pieces=input()
    if pieces=="Done":
        break

    m_pieces=int(pieces) 

    if room>=m_pieces:
        room=room-m_pieces
        baggage=baggage+m_pieces
    elif room==0:
       break
    else:
       baggage=baggage+m_pieces
       break


if total_room>=baggage:
 print(f"{room} Cubic meters left.")
elif total_room<baggage:
 left=total_room-baggage
 if left<0:
    left=abs(left)
 print(f"No more free space! You need {left} Cubic meters more.")
