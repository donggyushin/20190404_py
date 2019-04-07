# global 로 선언한 s 는 어디서 호출해서 사용해도 같은 메모리 어드레스에 접근하여 사용할 수 있음
# 많이 쓰지 않는 것이 좋다. 
def f():
    global s
    s = "I Love London!"
    print(s)


def main():
    f()
    print(s)
if __name__=="__main__":
    main()
