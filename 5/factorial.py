# n! 값을 구해주는 재귀함수. 
# 사람이 생각하는 것과 비슷하게 코드를 작성할 수 있어 코드 작성에는 쉽지만
# 스택에 많은 함수가 쌓여지게 되므로 효율적인 면에서는 불리할 수 있음. 
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    print(factorial(int(input("Input Number for Factorial Calculation: "))))
if __name__=="__main__":
    main()
