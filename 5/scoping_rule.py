def test(t):
    print(x)
    t=20
    print("In Function:", t)

x=10
test(x)
print("In Main:", x)
print("In Main:", y)    # t는 main함수 scope 안에 들어있지 않아서 호출불가