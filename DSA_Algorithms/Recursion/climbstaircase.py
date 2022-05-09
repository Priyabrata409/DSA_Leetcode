def climb_stairs(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        return climb_stairs(num-1) + climb_stairs(num - 2)


if __name__ == '__main__':
    print(climb_stairs(4))

