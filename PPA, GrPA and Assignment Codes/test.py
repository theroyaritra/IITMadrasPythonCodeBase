a,k=int(input()),1
ki=a
while k<=a:
  for i in range(1,k+1):
    if i<k:
      print(i, end=',')
    else:
      print(i)
  k=k+1
if k==a+1:
  ki=a-1
while ki<a:
  for j in range (1,ki+1):
    if j<ki:
      print(j,end=',')
    else:
      print(j)
  ki=ki-1