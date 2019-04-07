# 인수로 전달받은 값의 제곱을 반환함, 전달받은 인수x의 값은 3에서 5로 바뀔 것 같지만 바뀌지 않음. 
# f(x)라는 함수 안에서만 값이 바뀜
def f(x):
    y=x
    x=5
    return y*y


def main():
    x=3
    print(f(x))
    print(x)
if __name__=="__main__":
    main()
