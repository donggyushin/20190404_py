def asterisk_test(a, b, *args):
    return a+b+sum(args)


def main():
    print(asterisk_test(1, 2, 3, 4, 5))


if __name__ == "__main__":
    main()
