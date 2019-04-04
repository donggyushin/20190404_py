def print_something(my_name, your_name):
    print("Hello {}, my name is {}".format(your_name, my_name))

def main():
    print_something("Sungchul", "TEAMLAB")
    print_something(your_name="TEAMLAB", my_name="Sungchul")
    # 매개변수를 직접 지정해서 넣어준다. 

if __name__=="__main__":
    main()