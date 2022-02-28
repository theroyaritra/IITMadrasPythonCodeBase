#There is a limit to the number of recursions that can be computed in python. So, keep in mind that number of recursions should not exceed that limit, for the recursive Binary Search to run successfully
#Once again, this kind of Binary search will only run successfully on lists, that have been sorted in ascending order.
def recursive_BinarySearch(l,k,begin,end):
    if(begin==end):
        if(l[begin]==k):
            return True
        else:
            return False
    if(end-begin == 1): #if end and begin are consecutive indices
        if(l[begin]==k or l[end]==k):
            return True
        else:
            return False
    if(end-begin > 1):
        mid=(begin+end)//2
        if(l[mid]>k):
            end=mid-1
        elif(l[mid]<k):
            begin=mid+1
        else:
            return True
    if(end-begin < 0):
        return False
    return recursive_BinarySearch(l,k,begin,end)

arr=[5,-9,85,5,3,6,48,96,-8565,255,5,77,15,530]
arr.sort()
print(recursive_BinarySearch(arr,96,0,len(arr)-1))
print(recursive_BinarySearch(arr,255,0,len(arr)-1))
print(recursive_BinarySearch(arr,94,0,len(arr)-1))

l=list(range(10000*10000))
print(recursive_BinarySearch(l,9548450,0,len(l)-1))