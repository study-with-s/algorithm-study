# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
from collections import deque

input = sys.stdin.readline
write = sys.stdout.write

count = int(input())
queue = deque()
results = []

for _ in range(count):
    command = input().split()
    
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        results.append(str(queue.popleft() if queue else -1))
    elif command[0] == 'size':
        results.append(str(len(queue)))
    elif command[0] == 'empty':
        results.append(str(1 if not queue else 0))
    elif command[0] == 'front':
        results.append(str(queue[0] if queue else -1))
    elif command[0] == 'back':
        results.append(str(queue[-1] if queue else -1))

write('\n'.join(results) + '\n')