import matplotlib.pyplot as plt
import numpy as np

x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)


a=np.array([1,3,5,7,9,11,13,15,17])
b=np.array([84,86,88,90,92,94,96,98,100])
plt.plot(a,b,color='red',marker='.')

plt.show() # First it will show the scatter plot and the line graph together

#Bar Charts:-
m=np.array(['A','B','C','D'])
n=np.array([3,8,1,10])
plt.bar(m,n)
plt.show() #Secondly, it will show this bar graph
plt.barh(m,n)
plt.show() #Next, it will show the Horizontal Bar graph

#Histograms:-
x=np.random.normal(170,10,250) #This is the way to generate random numbers using numpy
plt.hist(x)
plt.show() # Next it will show the histogram

#Pie Charts:-
p=np.array([35,25,25,15])
myLabels=["Apples","Bananas",'Cherries','Dates']
plt.pie(p,labels=myLabels,startangle=90)
plt.show()

#Code for Matplotlib subplots not included here as it is explained too fast in video. Link to learn Matplotlib subplots properly:-
#https://www.youtube.com/watch?v=XFZRVnP-MTU&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=10