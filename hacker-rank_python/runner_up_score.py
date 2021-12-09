# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

arr.sort()
while n > 0:
    if arr[n-1] != arr[n-2]:
        print(arr[n-2])
        break
    else:
        n -= 1
