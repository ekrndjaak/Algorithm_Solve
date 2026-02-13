import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
total = 0

for _ in range(n):
    a, b = list(map(int, input().split()))
    total = total + (a * b)

print("Yes" if total == x else "No")