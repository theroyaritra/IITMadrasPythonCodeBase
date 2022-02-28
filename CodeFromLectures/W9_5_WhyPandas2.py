#Using Pandas:- (Easier and better)
import pandas as pd
scores=pd.read_csv("ExamScores.csv")
#total=[]
scores['Total']=scores['Chemistry Scores']+scores['Maths Scores']+scores['Chemistry Scores'] #We form a new coloumn Total without affecting the original .csv file in any way
print(scores['Maths Scores'].max())
print(scores['Physics Scores'].min())
print(scores['Chemistry Scores'].min())
print(scores['Total'].min())
#print(max(total))
print(scores.shape) #Gives the number of rows,coloumns in the form of a tuple
print(scores.count()) #Gives the count(number) of data in each coloumn
print("\nThe average score in Maths is = ",scores['Maths Scores'].mean())
print("The average score in Physics is = ",scores['Physics Scores'].mean())
print("The average score in Chemistry is = ",scores['Chemistry Scores'].mean())
print("The average total score of all the students is = ",scores['Total'].mean())
print("The total of all the scores in Physics is =", scores['Physics Scores'].sum())
print("\n")
print(scores['Maths Scores'].sort_values()) #Prints sorted list in ascending order of 'Maths Scores' values
print(scores['Total'].sort_values(ascending=False)) #Prints sorted list in descending order of 'Total' values

