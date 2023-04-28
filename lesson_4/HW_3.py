CamelCase_1 = ["FirstItem", "FriendsList", "MyTuple"]
CamelCase_2 = (' '.join(CamelCase_1))
camelcase_to_underscore = ''.join(['_'+letter.lower() if letter.isupper() else letter for letter in CamelCase_2])
snake = [word.strip('_') for word in camelcase_to_underscore.split()]
print(snake)
