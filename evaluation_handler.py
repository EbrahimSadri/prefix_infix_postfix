from constants import expression_format
from conversion_handler import in2pre, pre2post, post2in

def eval_handler(expr, exp_format):

    if check_eval_possibility(expr):
        validity = evaluate_expression(expr, exp_format)
        if not validity:
            print("\n\tEvaluation not possible")
            return False
    return True

# check if expression can be evaluated
def check_eval_possibility(expr):
    for x in expr:
        if x.isalpha():
            print("\n\tEvaluation not possible as input contains letters")
            return False
    return True

# evaluate expression based on which foramt it is
def evaluate_expression(expr, exp_format):
    global expression_format

    if exp_format == expression_format[2]:        
        validity = eval_postfix(expr, exp_format)
    elif exp_format == expression_format[0]:
        validity = eval_prefix(expr, exp_format)
    else:
        validity = eval_expr(expr, expr, exp_format)

    return validity
    

# infix expression formatter
def eval_expr(expr, in_expr, expr_format):

    try:
        evaluated_expression = eval(in_expr)
    except:
        print("\n\tCan not be evaluated")
        return False
    else:
        print("\n\tThe {} expression\
        \n\t-----------------------------------------------\
        \n\t{}\
        \n\t-----------------------------------------------\
        \n\tis equals to\
        \n\t===============================================\
        \n\t---> {}\
        \n\t===============================================\
        ".format(expr_format, expr, evaluated_expression))
    return True


# prefix expression formatter
def eval_prefix(expr, expr_format):

    # convert to infix
    valid, new_expr = pre2post(expr)
    if not valid:
        return False
    else:
        valid, in_expr = post2in(new_expr)
        if not valid:
            return False
        else:
            check_out = eval_expr(expr, in_expr, expr_format)
            if not check_out:
                return False
    return True


# postfix expression formatter
def eval_postfix(expr, expr_format):

    # convert to infix
    valid, in_expr = post2in(expr)
    if not valid:
        return False
    else:
        check_out = eval_expr(expr, in_expr, expr_format)
        if not check_out:
            return False
    return True
