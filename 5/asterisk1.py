# args라는 이름으로 가변인수를 받아와서 a,b,*args 인수들의 모든 합을 구해주는 함수
# 가변인수 *는 python3 부터 사용 가능. 
def asterisk_test(a, b, *args):
    return a+b+sum(args)


def main():
    print(asterisk_test(1, 2, 3, 4, 5))


if __name__ == "__main__":
    main()
