import math
# math라는 파이썬 기본 내장 모듈을 사용하기 위해서 미리 import 해주고 있다. 
a=1
b=-2
c=1
# sqrt() 함수는 0 이상의 x 에 한정해서 x의 제곱근값을 반환해주는 함수이다. 
print((-b + math.sqrt(b ** 2 - (4*a*c))) / (2*a) )
print((-b - math.sqrt(b**2-(4*a*c))) / (2*a) )
