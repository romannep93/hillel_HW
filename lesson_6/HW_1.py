number = int(input('Enter number: '))

if number > 0 and (number & (number-1)) == 0:
    print("YES")
else:
    print("NO")
