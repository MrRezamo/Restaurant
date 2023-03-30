from collections import deque

# read the number of operations
n = int(input())

# create an empty deque
d = deque()

# perform the operations
for i in range(n):

    operation = input().split()
    if operation[0] == 'append':
        d.append(int(operation[1]))
    elif operation[0] == 'appendleft':
        d.appendleft(int(operation[1]))
    elif operation[0] == 'pop':
        d.pop()
    elif operation[0] == 'popleft':
        d.popleft()

# print the elements of deque
print(*d)

