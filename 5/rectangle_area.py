# 가로와 너비를 입력받으면 해당 사각형의 넓이를 반환해주는 함수이다. 
def calculate_rectangle_area(x,y):
    return x * y



def main():
    rectangle_x = 10
    rectangle_y = 20
    print("사각형 x의 길이:", rectangle_x)
    print("사각형 y의 길이:", rectangle_y)

    # 넓이를 구하는 함수 호출
    print("사각형의 넓이:", calculate_rectangle_area(rectangle_x, rectangle_y))

if __name__ == '__main__':
    main()
