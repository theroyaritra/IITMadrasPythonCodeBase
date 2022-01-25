# Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output.
nums=input()
nums=nums.split(',')
max=int(nums[0])
for n in nums:
    if(int(n)>max):
        max=int(n)
print(max)
