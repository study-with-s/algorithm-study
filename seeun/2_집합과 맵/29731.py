promise = {'Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop'}

def isItChange (str):
    isItOK = True
    for i in range(len(str)):
        if str[i] not in promise:
            print("Yes")
            isItOK = False
            break
    if(isItOK):
        print("No")

def main():
    num = int(input())
    S_list = []
    for _ in range(num):
        S = input()
        S_list.append(S)
    
    isItChange(S_list)

if __name__ == "__main__":
    main()
