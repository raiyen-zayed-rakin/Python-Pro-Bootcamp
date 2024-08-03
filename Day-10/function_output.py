def my_function():
    return 3*2


res = my_function()
print(res)


def format_name(f_name, l_name):

    # f_name.title()
    # l_name.title()
    formatted_f = f_name.title()
    formatted_l = l_name.title()
    return formatted_f+" "+formatted_l
    # print("After return")


print(format_name("rakin", "zayed"))

