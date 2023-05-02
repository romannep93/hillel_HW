def change_list():
    user_input = input("Enter the list separated by commas: ")
    user_list = user_input.split(",")

    if len(user_list) < 2:
        print("The list must contain at least 2 elements")
    elif ' ' in user_list or '' in user_list and len(user_list) <=2:
        print("The list must contain at least 2 elements")
    else:
        user_list[0], user_list[-1] = user_list[-1], user_list[0]
        print(user_list)


change_list()