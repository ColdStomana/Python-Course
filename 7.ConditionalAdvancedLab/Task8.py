import math

hour_exam=int(input())
minute_exam=int(input())
hour_arrival=int(input())
minute_arrival=int(input())

arival=""

exam_minutes=hour_exam*60+minute_exam
arival_minutes=hour_arrival*60+minute_arrival 
diff=exam_minutes-arival_minutes
minutes=abs(diff)%60

hours=abs(diff)//60

if 0<=diff<=30: 
     arival="On time"
     print(f"{arival}")
     if diff !=0:
      print(f"{minutes} minutes before the start")
elif 30<diff<60 :
 arival="Early" 
 print(f"{arival}")
 print(f"{minutes} minutes before the start")
elif 60<=diff:
 arival="Early" 
 print(f"{arival}")
 print(f"{hours}:{minutes:02d} hours before the start")    
elif 0>diff>-60:
 arival="Late"
 print(f"{arival}")
 print(f"{minutes} minutes after the start")
elif -60>=diff:
 arival="Late"
 print(f"{arival}")
 print(f"{hours}:{minutes:02d} hours after the start")  


