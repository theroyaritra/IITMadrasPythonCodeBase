#Using FileHandling:-
f=open("ExamScores.csv",'r')
scores=f.readlines()[1:]
maths_max,physics_max,chemistry_max,total_max=0,0,0,0
maths_min,physics_min,chemistry_min,total_min=0,0,0,0
maths,chemistry,physics,total={},{},{},{}
for i in range(0,101):
    maths[i]=[]
    chemistry[i]=[]
    physics[i]=[]
for i in range(0,301):
    total[i]=[]
for record in scores:
    s=record.split(',')
    x=int(s[6])+int(s[7])+int(s[8])
    total[x].append(s[0])
    maths[int(s[6])].append(s[0])
    physics[int(s[7])].append(s[0])
    chemistry[int(s[8])].append(s[0])
for i in range(0,101):
    if(maths[i]==[]):
        del maths[i]
    if(physics[i]==[]):
        del physics[i]
    if(chemistry[i]==[]):
        del chemistry[i]
for i in range(0,301):
    if(total[i]==[]):
        del total[i]
total_max=max(total.keys())
maths_max=max(maths.keys())
physics_max=max(physics.keys())
chemistry_max=max(chemistry.keys())
maths_min=min(maths.keys())
physics_min=min(physics.keys())
chemistry_min=min(chemistry.keys())
total_min=min(total.keys())
    
print(maths[maths_max]," got the highest marks in maths = ",maths_max)
print(physics[physics_max]," got the highest marks in physics = ",physics_max)
print(chemistry[chemistry_max]," got the highest marks in chemistry = ",chemistry_max)
print(total[total_max]," got the highest marks in total = ",total_max)
print(maths[maths_min]," got the lowest marks in maths = ",maths_min)
print(physics[physics_min]," got the lowest marks in physics = ",physics_min)
print(chemistry[chemistry_min]," got the lowest marks in chemistry = ",chemistry_min)
print(total[total_min]," got the lowest marks in total = ",total_min)
f.close()