n=int(input())
scores_dataset=[]
d={}
for i in range(n):
    d['Name']=input()
    d['City']=input()
    d['SeqNo']=int(input())
    d['Mathematics']=int(input())
    d['Physics']=int(input())
    d['Chemistry']=int(input())
    scores_dataset.append(d)
    d={'Name':'','City':'','SeqNo':-1,'Mathematics':-1,'Physics':-1,'Chemistry':-1}


