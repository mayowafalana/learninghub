ls = ["+", "*", "/", "-"]
while True:
    vDigit1 = (input("Please input your 1st number:\n"))
    vOperator = str(input(
        "Please enter your operator. for Add press +, for Subtraction press - for Multiplication press * for division press /:\n"))
    if vOperator not in ls:
        print("Please try and enter the valid operator in this list [+, *, /, -] ")
    vDigit2 = (input("Please input your 2nd number:\n"))
    if vOperator == str("+"):
        print(int(vDigit1) + int(vDigit2))
    elif vOperator == str("-"):
        print(int(vDigit1) - int(vDigit2))
    elif vOperator == str("*"):
        print(int(vDigit1) * int(vDigit2))
    elif vOperator == str("/"):
        print(int(vDigit1) / int(vDigit2))
    next_cal = input("You still want to continue please yes to continue or no to stop")
    if next_cal == 'no':
        break
