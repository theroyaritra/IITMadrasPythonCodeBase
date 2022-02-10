dic={} #Basic syntax of dictionary data structure. If elements are included within {} then, it becomes a set data structure.
dic['aritra']=6295666946
dic['abhijit']=9474071064
dic['sutapa']=8145695936
print(dic)
print(dic['aritra']) #Here dic[0], dic[1] won't work. We have to specify the proper key.
malgudi=['It','was','Monday','morning','Swaminathan','was','reluctant','to','open','his','eyes','He','considered','Monday','specially','unpleasant','in','the','calendar','After','the','delicious','freedom','of','Saturday','and','Sunday','it','was','difficult','to','get','into','the','Monday','mood','of','work','and','discipline','He','shuddered','at','the','very','thought','of','school:','the','dismal','yellow','building:','the','fire','eyed','Vedanayagam','his','class','teacher','and','headmaster','with','his','thin','long','cane']
print(len(malgudi))
s=set(malgudi)
print(s) #All repeated words will be gone
print(len(s))
malgudi[47]="school"
malgudi[51]="building"
print(malgudi)
print("\n")
# Using dictionary to find the frequency of all words in the list malgudi:-
d={}
s=set(malgudi)
for x in s:
    d[x]=0 #Initialization of the dictionary
for x in malgudi:
    d[x]=d[x]+1
print(d)
#Using dictionary to find the word repeated maximum number of times in the list malgudi:-
max=0
maxWord=''
for x in malgudi:
    if(d[x]>max):
        max=d[x]
        maxWord=x
print('\nThe word "',maxWord, '" has been repeated the maximum number of times in the list malgudi. It has been repeated for a total of %d times.'%(max))
#Example of storing lists within dictionary:- [We can even store dictionary within dictionary]
a={}
a['Aritra']=[90,85,96,"theroyaritra@gmail.com"]
a['Madhura']=[85,63,95,'madhura123@hotmail.com']
a['Pratik']=[56,96,95,'pratik_super@yahoo.co.in']
print(a)
print(a['Aritra'][1])
print(a['Pratik'][3])