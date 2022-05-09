def print_counting(num: int) -> None:
    if num == 0:
        return
    else:
        print_counting(num - 1)
        print(num)

def print_counting_reverse(num: int) -> None:
    if num == 0:
        return
    else:
        print(num)
        print_counting(num - 1)


if __name__ == '__main__':
    num = 10
    print_counting(num)