import pandas as pd
scores=pd.read_csv("ExamScores.csv")
scores['Total']=scores['Chemistry Scores']+scores['Maths Scores']+scores['Chemistry Scores']

print(scores['Names'],type(scores['Names']),"\n") #These are known as Pandas Series
print(scores.head()) #Prints first 5 rows of the Dataframe
print(scores.tail()) #Prints last 5 rows of the Dataframe
print("\n",scores[scores['Names']=="Aritra Roy"],"\n")

print(scores[scores['gender']=="male"]["Total"].max()) #prints maximum total marks by a male
print(scores[scores['gender']=="male"]["Total"].min()) #prints minimum total marks by a male
print(scores[scores['gender']=="female"]["Total"].min()) #prints minimum total marks by a female
print(scores[scores['gender']=="female"]["Total"].max()) #prints maximum total marks by a female

#Program to divide students into groups based on their marks:-
print('\n')
'''
print(scores[scores['Physics Scores']>85].shape[0]," students got A grade in Physics")
print(scores[scores['Physics Scores'].between(70,85)].shape[0]," students got B grade in Physics")
print(scores[scores['Physics Scores'].between(60,70)].shape[0]," students got C grade in Physics")
print(scores[scores['Physics Scores']<60].shape[0]," students got D grade in Physics")

print(scores[(scores['gender']=='female') & (scores['Chemistry Scores']>85)].shape[0]," female students got A grade in Chemistry")
print(scores[(scores['gender']=='male') & (scores['Chemistry Scores']>85)].shape[0]," male students got A grade in Chemistry")
'''
#Note: Pandas doesn't support regular Python 'and' operator. Here, and operator is denoted by '&'
subject=['Maths Scores','Physics Scores','Chemistry Scores']
for sub in subject:
    avg=scores[sub].mean()
    print(scores[(scores['gender']=='male') & (scores[sub]>85)].shape[0]," male students got A grade(above 85) in", sub.split()[0])
    print(scores[(scores['gender']=='male') & (scores[sub]>avg)].shape[0]," male students got above the average marks of", avg, "in", sub.split()[0])
    print(scores[(scores['gender']=='female') & (scores[sub]>85)].shape[0]," female students got A grade(above 85) in ",sub.split()[0])
    print(scores[(scores['gender']=='female') & (scores[sub]>avg)].shape[0]," female students got above the average marks of", avg, "in", sub.split()[0])
print(scores[(scores['gender']=='female') & (scores['Total']>85)].shape[0]," female students got A grade(above 85) in Total")
print(scores[(scores['gender']=='male') & (scores['Total']>85)].shape[0]," male students got A grade(above 85) in Total")