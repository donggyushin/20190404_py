import math
# 파이선 기본 내장 모듈인 math 를 사용하기 위해서 import 해주고 있다. 
# import문은 항상 파일의 가장 윗줄에다가 선언해준다. 


def get_result_quadratic_equation(a,b,c):
	values=[]
	# append() 메서드는 이미 존재하고 있는 list에 한개의 아이템을 덧붙여주는 
	# 함수이다. 새로운 리스트를 반환하진 않는다. 
	# 기존에 존재하는 list 를 재정의해준다. 
	values.append((-b + math.sqrt(b ** 2 - (4 * a * c))) / (2*a))
	values.append((-b - math.sqrt(b**2-(4*a*c))) / (2*a))
	return values

print(get_result_quadratic_equation(1,-2,1))
