import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = [num for num in arr if num < x]
print(*result)