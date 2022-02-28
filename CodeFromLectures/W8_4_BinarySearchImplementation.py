# Only condition for these kind of binary searches to run successfully is that the list has to be sorted in the Ascending order:-
def binary_search1(l,k): #Logic of IITM by Prof. Iyengar
    begin=0
    end=len(l)-1
    mid=0
    while(end-begin>1):
        mid=(begin+end)//2
        if(l[mid]==k):
            return True
        if(l[mid]>k):
            end=mid-1
        if(l[mid]<k):
            begin=mid+1
    if(l[begin]==k or l[end]==k): #For the condition when either begin>end or, end-begin <= 1 i.e. end-begin = 0 or 1
        return True
    return False #If we reach here, it implies element has not been found at all
l=[12,15,85,96,-85,69,5,6,38,2,9,-46,82,6,200]
l.sort()
print(binary_search1(l,58))
print(binary_search1(l,5))
print(binary_search1(l,38))
print(binary_search1(l,15))

def binary_search2(arr, x): #Simple and standard logic that gives you direct index of element if found
	begin = 0
	end = len(arr) - 1
	mid = 0
	while (begin <= end):
		mid = (end + begin) // 2
		# If x is greater, ignore left half
		if arr[mid] < x:
			begin = mid + 1
		# If x is smaller, ignore right half
		elif arr[mid] > x:
			end = mid - 1
		# means x is present at mid
		else:
			return mid
	# If we reach here, then the element was not present
	return -1

arr = [ 2, 3, 4, 10, 40, -85, 69 , -8569, -58, 52, 63 ]
arr.sort()
result = binary_search2(arr, -85695)
result = binary_search2(arr,10)
if result != -1:
	print("In the list sorted in ascending order, element is present at index ", str(result))
else:
	print("Element is not present in the list")
