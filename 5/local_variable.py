# f() 함수 내에서의 s 와 f() 함수 외부에서의 s 는 같은 변수명을 가지고 있지만 엄연히
# 다른 메모리 주소값을 가지고 있기 때문에 다른 변수이다. 
def f():
    s="I Love London!"
    print(s)

s = "I Love Paris!"
f()
print(s)

