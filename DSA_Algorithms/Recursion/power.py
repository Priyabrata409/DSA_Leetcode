def power(num: int, p: int):
    if p == 0:
        return 1
    else:
        return num * pow(num, p-1)


if __name__ == '__main__':
    num, p = 10, 3
    print(power(num,p))

