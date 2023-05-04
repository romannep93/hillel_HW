def change_list(lst):
    if len(lst) < 2:
        print("The list must contain at least 2 elements")
    else:
        lst[0], lst[-1] = lst[-1], lst[0]
        print(lst)


change_list(["apple", "banana", "cherry"])
