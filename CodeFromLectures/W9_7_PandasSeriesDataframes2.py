import pandas as pd
scores=pd.read_csv("ExamScores.csv")
print(scores.groupby('gender').groups) #Gives a dictionary of lists of the index numbers of the keys under 'gender'
subject=['Maths Scores','Physics Scores','Chemistry Scores']
for sub in subject:
    print("Students above Average in ", sub, " are:-")
    avg=scores[sub].mean()
    print(scores[scores[sub]>avg].groupby('gender').groups)