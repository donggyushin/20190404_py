def f():
    global s
    s = "I Love London!"
    print(s)


def main():
    f()
    print(s)
if __name__=="__main__":
    main()