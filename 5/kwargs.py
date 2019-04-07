# 파이썬 프로그래머들이 * 와  ** 에 대해서 이해하는데 꾀나 혼동을 한다. 
# 물론 나도 마찬가지. *args와 **kwargs는 무엇일까? 한가지 짚고 넘어가야 할게 이것들은
# 프로그래밍을 하는데에 있어서 필수적인 요소는 아니다. 
# 오직 *(asterisk)만이 필수적인 요소이다. 꼭 *args, **kwargs 라고 써야하는 것도 아니다. 
# *var, **vars 이런식으로 쓰는것도 가능하다. 
# *args 에 대해서 먼저 살펴보자. 
# 우선 *args 와 **kwargs 는 함수를 정의할때에 주로 사용된다. *args 와 **kwargs 는 
# 함수에 여러개의 변수들을 전달하는데에 사용된다. 
# 여기서 의미하는 변수란 유저에의해서 얼마나 많은 변수들이 함수에 전달되어질지 모르는 변수들이다. 
# *args 는 non-keywarded 변수 리스트가 함수에 전달되어질때 사용된다. 
# **kwargs에 대해서 살펴보자. 
# **kwargs는 이미 눈치챘겠지만 keyworded 변수 리스트가 함수에 전달되어질 수 있게 해준다. 
# 만약에 고유이름을 가지고 있는 변수들을 함수에서 다루고 싶다면 *args 대신에 **kwargs 를 
# 사용하면 된다. 
def kwargs_test(**kwargs):
	print(kwargs)
	print("First value is {first}".format(**kwargs))
	print("Second value is {second}".format(**kwargs))
	print("Thirs value is {third}".format(**kwargs))

kwargs_test(first=3, second=4, third=5)
