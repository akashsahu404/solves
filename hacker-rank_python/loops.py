# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print square of n.

n = int(input("Enter value of n: "))
for i in range(0, n):
    print(str(i**2))
