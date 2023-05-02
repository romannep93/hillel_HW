def to_dict(lst):
    return {elem: elem for elem in lst}


lst = input("Enter the list separated by commas: ").split(',')
print(to_dict(lst))
