def fibonacci(pth: int) -> int:
    if pth == 0:
        return 0
    elif pth == 1:
        return 1
    else:
        return fibonacci(pth - 1) + fibonacci(pth - 2)


if __name__ == '__main__':
    pth = 10
    print(fibonacci(3))