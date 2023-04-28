program_lang = {'python': 'Guido van Rossum',
                'php': 'Rasmus Lerdorf',
                'java': 'James Arthur Gosling',
                'c++': 'Bjarne Stroustrup'}
for k, v in program_lang.items():
    print('My favorite programming language is ' + k + '.It was created by ' + program_lang[k])
del(program_lang['c++'])
print(program_lang)
