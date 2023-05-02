def sum_range(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for num in range(start, end + 1):
        total += num
    return total


while True:
    user_input = input("Enter two numbers separated by commas: ")
    input_values = user_input.split(",")

    if len(input_values) == 2:
        start, end = input_values
        start = int(start.strip())
        end = int(end.strip())
        break
    else:
        print("Enter exactly two numbers")

result = sum_range(start, end)
print(result)
