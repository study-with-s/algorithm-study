def addTemp(stack, temp):
    if stack:
        temp.append(stack.pop())
    return

def removeTemp(stack, temp):
    if temp:
        stack.append(temp.pop())
    return

def main(keyLog):
    stack = []
    temp = []

    for i in keyLog:
        if i == '<':
            addTemp(stack, temp)
        elif i == '>':
            removeTemp(stack, temp)
        elif i == '-':
            if stack:
                stack.pop()
        else:
            stack.append(i)

    # 마지막에 남은 temp가 있다면 stack에 추가
    while temp:
        stack.append(temp.pop())
    
    result = ''.join(stack)
    print(result)

if __name__ == "__main__":
    count = int(input())

    keyLogs = []
    for i in range(count):
        keyLogs.append(input())

    for keyLog in keyLogs:
        main(keyLog)