'''
# Even after applying sys.stdin() and sys.stdout(), this solution is getting TLE! So, its not the optimized solution.
import sys
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    l=list(map(int,sys.stdin.readline().split()))
    q=int(sys.stdin.readline())
    trip=[]
    for i in range(q):
        q1,q2=map(int,sys.stdin.readline().split())
        trip.append([q1,q2])
    for e in trip:
        sum=0
        for i in range(e[0],e[1]+1):
            sum=sum+l[i-1]
        sys.stdout.write(str(sum)+"\n")
'''
#Optimized code:-
import sys
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    l=list(map(int,sys.stdin.readline().split()))
    q=int(sys.stdin.readline())
    p=[]
    s=0
    for i in range(len(l)):
        s=s+l[i]
        p.append(s)
    for i in range(q):
        q1,q2=map(int,sys.stdin.readline().split())
        if(q1==1):
            sys.stdout.write(str(p[q2-1]) + "\n")
        else:
            sys.stdout.write(str(p[q2-1]-p[q1-2]) + "\n")