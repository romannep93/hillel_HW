class FormulaError(Exception):
    pass


def calculator():
    try:
        formula = input("Enter a formula (e.g. 1 + 1): ")
        elements = formula.split()

        if len(elements) != 3:
            raise FormulaError("Invalid formula")

        num1 = float(elements[0])
        num2 = float(elements[2])

        if elements[1] not in ["+", "-"]:
            raise FormulaError("Invalid operator")

        if elements[1] == "+":
            result = num1 + num2
        else:
            result = num1 - num2

        print("Result:", result)

    except FormulaError as fe:
        print("Formula Error:", fe)
    except ValueError:
        print("Formula Error: Invalid number")


calculator()
