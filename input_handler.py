from constants import operators, expression_format

# main function for input handler returns input when valid
def input_handler_function():

    space_check = False
    bracket_space = False
    counter = 0
    while not space_check and not bracket_space:
        if counter != 0:
            print("\n\tInput Error Try agian")
            if not space_check:
                print("\tIncorrect Spacing in Input")
            if not bracket_space:
                print("\tBracket Imbalance in Input")
        expr = input_expression()
        space_check = check_space(expr)
        bracket_space = check_brackets(expr)
        counter += 1
    expr_format = check_format(expr)
    return [expr, expr_format]

# takes in any input
def input_expression():
    expr = input("\n\tInput Expression \n\
    \tAll elements in an expressions\n\
    \tshould have space betten each element \n\
    \t(eg: '5 + 3 * ( 9 - 2 )' ) \n\
    \t===============================================\n\t--> ")      

    expr = expr.strip()

    return expr

# checks validity of input
def check_space(expr):
    expr_list = expr.split(" ")

    no_operators = True
    no_alnum = True
    for x in expr_list:
        if x in operators.keys():
            no_operators = False
        if x.isalnum():
            no_alnum = False
    if no_operators or no_alnum:
        return False

    if not all(char for char in expr_list):
        return False

    for c, x in enumerate(expr):
        if x == expr[-1]:
            continue
        if x.isspace() or expr[c+1].isspace():            
            continue
        else:
            if x.isdigit() and expr[c+1].isdigit():
                continue
            else:
                return False
    return True

# check for brakcets imbalance
def check_brackets(expr):
    bracket_list = []
    for c, x in enumerate(expr):
        if x == "(":
            bracket_list.append(x)
        elif x == ")":
            if bracket_list:
                bracket_list.pop(-1)
            else:
                return False
    if not bracket_list:
        return False
    return True

# check which format expression is in 
def check_format(expr):
    global operators, expression_format

    if expr[0] in operators.keys():
        exp_format = expression_format[0]
    elif expr[-1] in operators.keys():
        exp_format = expression_format[2]
    else:
        exp_format = expression_format[1]

    print("\n\tExpression Format is ---> {}".format(exp_format))    

    return exp_format