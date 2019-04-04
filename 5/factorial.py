def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    print(factorial(int(input("Input Number for Factorial Calculation: "))))
if __name__=="__main__":
    main()