n = int(input())
arr = list(map(int, input().split()))
larger = max(arr)
for i in range(n):
    if larger == max(arr):
        arr.remove(max(arr))
print(max(arr))
