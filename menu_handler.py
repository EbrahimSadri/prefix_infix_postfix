import sys
from constants import expression_format
from conversion_handler import in2pre, pre2post, post2in
from evaluation_handler import eval_handler

def exit_handler():
    print("\n\n\t{} ------- END ------- {}\n\n")    
    sys.exit()

# ----------------- exit end ------------------------ #

# print expression
def print_expression(expr, old_format, new_expr, exp_format):
    print("\n\n\tThe {} expression \
    \n\t-----------------------------------------------\n\t{} \
    \n\t----------------------------------------------- \
    \n\tin {} is  \
    \n\t===============================================\n\t{} \
    \n\t===============================================\n \
    ".format(old_format, expr, exp_format, new_expr))

# ------------------- printer ------------------------ #

def show_menu(exp_format):
    
    print("\n")
    counter = 1 
    for exp_for in expression_format:
        if exp_for == exp_format:
            continue
        print("\tInput --> '{}' \t- to convert \
to '{}' expression".format(counter, exp_for.capitalize()))
        counter += 1
    print("\tInput --> '3' \t- to Evaluate expression")
    print("\tInput --> '4' \t- to Enter new expression")
    print("\tInput --> '5' \t- to Exit the code")

    choice = input("\n\tEnter Choice: \n\t---> ")

    return choice

# _________________ Choice Menu END _____________________ #

def act_on_input(user_input, exp_format, expr):    
    if int(user_input) < 3:

        # if prefix
        if exp_format == expression_format[0]:
            # convert to infix -> 1
            if user_input == "1":
                valid, new_expr = pre2post(expr)
                if not valid:
                    return False
                else:
                    valid, new_expr = post2in(new_expr)
                    if not valid:
                        return False
                    else:
                        print_expression(expr, exp_format, new_expr, expression_format[1])
            # convert to postfix -> 2
            if user_input == "2":
                valid, new_expr = pre2post(expr)
                if not valid:
                    return False
                else:
                    print_expression(expr, exp_format, new_expr, expression_format[2])
            pass

        # if infix
        elif exp_format == expression_format[1]:
            # convert to prefix -> 1
            if user_input == "1":
                valid, new_expr = in2pre(expr)
                if not valid:
                    return False
                else:
                    print_expression(expr, exp_format, new_expr, expression_format[0])              
            # convert to postfix -> 2
            if user_input == "2":
                valid, new_expr = in2pre(expr)
                if not valid:
                    return False
                else:
                    valid, new_expr = pre2post(new_expr)
                    if not valid:
                        return False
                    else:
                        print_expression(expr, exp_format, new_expr, expression_format[2])

        # if postfix
        else:
            # convert to prefix -> 1
            if user_input == "1":
                valid, new_expr = post2in(expr)
                if not valid:
                    return False
                else:
                    valid, new_expr = in2pre(new_expr)
                    if not valid:
                        return False
                    else:
                        print_expression(expr, exp_format, new_expr, expression_format[0])
            # convert to infix -> 2    
            if user_input == "2":
                valid, new_expr = post2in(expr)
                if not valid:
                    return False
                else:                    
                    print_expression(expr, exp_format, new_expr, expression_format[1])

    elif user_input == "3":        
        validity = eval_handler(expr, exp_format)
        if not validity:
            return False        
    elif user_input == "4":
        return False
    elif user_input == "5":
        exit_handler()
    else:
        return False

    return True

# _________________ Action on User Input END _____________________ #

