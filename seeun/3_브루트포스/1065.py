def abc(num, count):
    a = num//100
    b = (num//10)%10
    c = num%10

    if a - 2*b +c ==0 :
        return True

if __name__ == "__main__":
    num = int(input())
    if num < 99:
        print(num)
    else:
        count = 0
        for i in range(100, num + 1):
            if abc(i, count):
                count += 1
        print(99 + count)