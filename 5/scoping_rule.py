def test(t):
    print(x)
    # x는 전역변수이므로 test()함수 내에서도 호출 가능하다. 
    t=20
    # 여기서의 t 는 메인코드의 x변수의 메모리 주소값을 가지고 있는게 아니라	
    # value값만 가지고 접근하기 때문에 바깥 scope 에서는 접근이 불가능하다. 
    print("In Function:", t)

x=10
test(x)
print("In Main:", x)
print("In Main:", t)    # t는 main함수 scope 안에 들어있지 않아서 호출불가
