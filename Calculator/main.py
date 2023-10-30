
status = 'y'
first_time = True
first_number = 0
while status != 'n':
    if first_time == True:
        first_number = float(input("What is the first number? "))

    operation = input("+\n-\n*\n/\nPick an operation : ")
    second_number = float(input("What is the second number? "))
    result = 0
    if operation == '+':
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
    elif operation == '-':
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")
    elif operation == '*':
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
    if operation == '\\':
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    else:
        print(f"You have a problem.")
    first_number = result
    first_time = False
    status = input(f'Type \'y\' to continue calculating with {result} or type \'n\' to start a new calculation.')



