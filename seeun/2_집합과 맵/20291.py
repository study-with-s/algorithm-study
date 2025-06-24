
def main():
    count = int(input())
    exp_list = {}
    for _ in range(count):
        filename = input()
        exp = filename.split('.')[1]
        if exp not in exp_list:
            exp_list[exp] = 1
        else:
            exp_list[exp] = exp_list[exp] + 1
    sorted_exp_list = dict(sorted(exp_list.items()))

    for key, value in sorted_exp_list.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    main()
