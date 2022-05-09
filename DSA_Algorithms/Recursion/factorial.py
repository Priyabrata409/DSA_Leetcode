def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == '__main__':
    num = 10
    print(factorial(5))