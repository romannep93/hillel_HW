text = input(str('Enter text: '))
text_list = text.split(' ')
if len(text_list) < 3:
    print(f'The number of elements in the list is less than 3, your list length is {len(text_list)}')
else:
    print(text_list[-3], text_list[-2], text_list[-1])
