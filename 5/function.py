def f(x):
    return 2 * x + 7

def g(x):
    return x ** 2

# 고등학교 수학시간때 자주 보던 전형적인 함수 문제임. 
def main():
    x = 2
    print(f(x) + g(x) + f(g(x)) + g(f(x)))

if __name__ =="__main__":
    main()
