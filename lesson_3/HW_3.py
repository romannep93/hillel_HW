text = input(str('Enter string: '))
if 'abc' in text[0:3]:
    print(text.replace('abc', 'www'))
else:
    print(text+'zzz')
