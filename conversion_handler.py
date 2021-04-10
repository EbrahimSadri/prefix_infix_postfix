from constants import operators, expression_format

# postfix to infix
# convert input expr sting into list split by space
# adds all operands to list until an operator is found
# combines last 2 operands with operator with brackets
# and adds to expr list
# loops through entire list until entire expr converted
# removes extra brackets and bobs your uncle
# try and except to check validity of expression
# returns False if invalid input prompts for new input
def post2in(expr):
        
    operand_list = []    
    expr = expr.split(" ")
    for char in expr:
        if char.isalnum():
            operand_list.append(char)
        if char in operators.keys():
            try:
                temp = "( " + operand_list[-2] + " " + char + " " + operand_list[-1] + " )"
            except:
                print("\n\n\tOperand List empty, incorrect input")
                return [False, []]
            else:
                operand_list = operand_list[:-2]
                operand_list.append(temp)
    try:
        infix_expr = operand_list[0][1:-1].strip()  
    except:
        print("\n\n\tInfix Can't be proccessed incorrect input")
        return [False, []]
    else:
        pass  
    return [True, infix_expr]


# just refer this video on youtube 
# https://www.youtube.com/watch?v=8QxlrRws9OI
def in2pre(expr):

    prefix = []
    opstack = []

    expr = expr[::-1]
    expr = expr.split(" ")
    for counter, char in enumerate(expr):
        if char == "(":
            expr[counter] = ")"
        elif char == ")":
            expr[counter] = "("
        else:
            pass    
        if char.isalnum():
            prefix.append(char)
        elif char in operators.keys():
            if not opstack:
                opstack.append(char)
            else:            
                while opstack:
                    last_item = opstack[-1]
                    if last_item == ")":
                        opstack.append(char)
                        break
                    elif operators[char] > operators[last_item]:
                        opstack.append(char)
                        break
                    elif operators[char] == operators[last_item]:
                        if not char == "*":
                            opstack.append(char)
                            break
                        else:
                            prefix.append(opstack.pop(-1))
                            opstack.append(char)
                            break
                    else:
                        prefix.append(opstack.pop(-1))
                        opstack.append(char)
                        break                    
        else:
            if char == ")":
                opstack.append(char)
            elif char == "(":
                while opstack[-1] != ")":
                    prefix.append(opstack.pop(-1))
                opstack.pop(-1)
            else:
                pass
    while opstack:
        prefix.append(opstack.pop(-1))
    prefix = " ".join(prefix[::-1])
    return [True, prefix]



# prefix expression to postfix
# expression converted into list split based on space
# a while loop that loops until expression list only has 1 element
# that 1 element being the formatted postfix expression
# works by looping through all the list elements and finding operands
# when an operand is found it must have two consequtive elements ahead of it
# that are either an alnum or a formated segment of the expression
def pre2post(expr):
    
    expr = expr.split(" ")
    new_segement = ""

    while len(expr) != 1:
        for counter, char in enumerate(expr):
            if not counter < len(expr)-2:
                break
            if char in operators.keys():  
                try:
                    if not expr[counter+1] in operators.keys():
                        if not expr[counter+2] in operators.keys():
                            new_segement = expr[counter+1] + " "
                            new_segement = new_segement + expr[counter+2] + " " + char
                            for x in range(3):
                                expr.pop(counter)
                except:
                    print("\n\n\tInvalid Prefix Expression, Try again with new Input")
                    return [False, []]
                else:         
                    if new_segement:       
                        if counter != 0:
                            expr = expr[:counter] + [new_segement] + expr[counter:]
                        else:
                            expr = [new_segement] + expr
                        new_segement = ""
    return [True, expr[0]]

