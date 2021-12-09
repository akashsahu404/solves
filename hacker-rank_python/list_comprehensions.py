# You are given three integers x, y, z  and  representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n.

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
    
result = []
for left in range(x+1):
    for middle in range(y+1):
        for right in range(z+1):
            if left+middle+right != n:
                result.append([left, middle, right])
        
print(result)
