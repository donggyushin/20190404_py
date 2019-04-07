# x,y,z 의 모양을 확인할 수 있는 함수
# z는 배열임을 알 수 있음
def asterisk_test_2(*args):
	x,y,*z = args
	return x,y,z

print(asterisk_test_2(3,4,5,10,20))
