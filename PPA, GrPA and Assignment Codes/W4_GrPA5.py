# Important question
n = int(input())
L = [ ]
# Append all points in the sequence to the list L
for i in range(n):
    L.append(input())
# Point P
point = input().split(',')
x = int(point[0])
y = int(point[1])

# List to maintain all nearest points
min_list = []
min_dist = 1000
for i in range(n):
    # One of the points in the sequence
    temp = L[i].split(',')
    # Extract the x and y coordinates of this point
    temp_x = int(temp[0])
    temp_y = int(temp[1])
    # Compute the distance
    dist = ((x - temp_x) ** 2 + (y - temp_y) ** 2) ** 0.5
    # Check if it is the minimum distance
    if (dist < min_dist):
        min_dist = dist
        min_list = [L[i]]
    elif dist == min_dist:
        min_list.append(L[i])
for point in min_list:
    print(point)