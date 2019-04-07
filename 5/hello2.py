# 중복이 될만한 코드를 함수로 만들어와서
def print_hello():
	print("Hello World")
	print("Hello TEAMLAB")

a = 5
# 필요할때마다 호출하여 사용한다.
if(a>3):
	print_hello()
if (a>4):
	print_hello()
if(a>5):
	print_hello()


