names_list = ["John", "Marta", "James", "Amanda", "Marianna"]
name = 'NAME'.center(20, '*')
names_list = [i.rjust(20) for i in names_list]
names_list_new = ('\n'.join(names_list))
print(f'{name}\n{names_list_new}')
