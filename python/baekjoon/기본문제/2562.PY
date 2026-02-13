import sys
input = sys.stdin.readline

count = 0
index = 0

for i in range(9):
    num = int(input())

    if num > count:
        count = num
        index = i + 1

print(count)
print(index)