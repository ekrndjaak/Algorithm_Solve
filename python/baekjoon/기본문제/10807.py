import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
f = int(input())

print(arr.count(f))