# 매개변수를 전달받지 않는 사각형의 너비를 구하는 함수, 특정한 값을 반환하지는 않고 출력만 해줌
def a_rectangle_area():
    print(5*7)
# 가로와 세로의 길이를 아는 사각형의 너비를 구하는 함수, 특정한 값을 반환하지는 않고 출력만 해줌
def b_rectangle_area(x,y):
    print(x*y)
# 변수를 전달받지 않는 사각형의 너비를 구하는 함수. 특정한 값을 반환해줌. 
def c_rectangle_area():
    return(5*7)
# 가로와 세로의 길이를 아는 사각형의 너비를 구하는 함수, 특정한 값을 반환해줌. 
def d_rectangle_area(x,y):
    return x*y

def main():
    a_rectangle_area()
    b_rectangle_area(5,7)
    print(c_rectangle_area())
    print(d_rectangle_area(5,7))

if __name__=="__main__":
    main()
