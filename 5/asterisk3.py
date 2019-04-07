# x,y,z 의 모양을 알아보기 위한 함수
# z 같은 경우에는 배열임을 확인할 수 있음
def asterisk_test_2(*args):
    x, y, *z = args
    return x, y, z


print(asterisk_test_2(3, 4, 5))
