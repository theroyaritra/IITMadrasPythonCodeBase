def solution(L):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    sorted_L=[]
    while(len(L)>0):
        max=L[0]
        for i in range(len(L)):
            if(L[i]>max):
                max=L[i]
        sorted_L.append(max)
        L.remove(max)
    ### Enter your solution above this line
    return sorted_L
L=[1.1,2.2,3.3]
print(solution(L))