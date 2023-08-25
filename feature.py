#Priority scheduler 

import time
from datetime import date


print("Exams are approaching")
time.sleep(1)
print("Get some help")
time.sleep(2)
print("Let's get started")
time.sleep(2)
print("When is your exam")
exam_date=int(input("Enter date:"))
exam_month=int(input("Enter month:"))
exam_time=date(2023,exam_month,exam_date)

today=date.today()

left_days= exam_time - today
left_days=str(left_days)
op1=left_days.split(',')
left_days=op1[0]
print("You have ",left_days,"days left")

print("Let's see how we can prepare:")
time.sleep(1.2)
study_t=float(input("How many hours do you study:"))
time.sleep(1.2)
sub=int(input("How many subjects do you have:"))
hard_sub=int(input("How many ,you consider are hard subjects."))
print("You must give ",round((study_t/hard_sub),)," hours to every hard subject.")
print("You must give ",round((study_t/(sub-hard_sub)),1)," hours to rest per subject.")

ref={
    'Maths':['yt1_m','yt2_m','yt3_m'],
    'Physics':['p1','p2'],
    'Chemistry':['c1','c2']
}



