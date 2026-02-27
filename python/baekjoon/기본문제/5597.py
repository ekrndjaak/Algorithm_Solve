import sys
input = sys.stdin.readline

arr = set(range(1,31))

for _ in range(28):
    sub = int(input())
    arr.remove(sub)

for s in sorted(arr):
    print(s)