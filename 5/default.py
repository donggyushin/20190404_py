def print_something_2(my_name, your_name="TEAMLAB"):    # 아무것도 입력을 안받을시에 your_name에는 TEAMLAB이라는 값이 드루감
    print("Hello {}, my name is {}".format(your_name, my_name))

print_something_2("Sungchul", "TEAMLAB")
print_something_2("Sungchul")