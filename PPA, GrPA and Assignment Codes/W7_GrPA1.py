''' My own Code:-

d={'CSK':0,'DC':0,'KKR':0,'MI':0,"PK":0,'RCB':0,'RR':0,'SH':0}
x={}
for i in range(8):
    s=input().split(',')
    for key in d:
        if(s[0]==key):
            d[key]+=len(s)-1
x=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
for key in x:
    print(key,d[key],sep=':')

'''
# This question is very important to understand how to sort a dictionary based on its values
# IIT Madras Solution Code:- [Better and easy-to-grasp logic]
results = [ ]
for i in range(8):
    L = input().split(',')
    winner = L[0]       # the first team is the winner
    losers = L[1: ]     # all these teams have lost to the winner
    # we only need the number of wins and the winning team
    results.append((winner, len(losers)))

table = [ ]
# two-level-sort
# refer GrPA-4 of week-6
# we first sort by points, then by name
while results != [ ]:
    maxteam = results[0]
    for i in range(len(results)):
        team = results[i]
        if team[1] > maxteam[1]:
            maxteam = team
        elif team[1] == maxteam[1] and team[0] < maxteam[0]:
            maxteam = team
    results.remove(maxteam)
    table.append(maxteam)

for team in table:
    print(f'{team[0]}:{team[1]}')