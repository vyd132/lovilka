import random

ych1={"Name":"Ivan","Age":12,"Height":157}
ych2={"Name":"Anton","Age":13,"Height":153}
ych3={"Name":"Sergey","Age":12,"Height":162}
ych4={"Name":"Vladimir","Age":11,"Height":154}
ych5={"Name":"Grigory","Age":14,"Height":157}
allych=[ych1,ych2,ych3,ych4,ych5]
for age in allych:
    age["Age"]+=1

for date in allych:
    date_birth=2024-date["Age"]
    date["Date_of_birth"]=date_birth

for dist in allych:
    dist["Distation"]=random.randint(55,155)

print(allych)