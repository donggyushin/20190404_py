# 가변인수 args 의 이름을 확인해보기 위한 함수
def asterisk_test(a, b, *args):
    print(args)


def main():
    print(asterisk_test(1, 2, 3, 4, 5))


if __name__ == "__main__":
    main()
