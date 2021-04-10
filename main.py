import sys
from input_handler import input_handler_function
from menu_handler import show_menu, act_on_input

print("\n")
# --------------------------------- Main ---------------------------------

while True:
    
    # input expression
    expression, expression_format = input_handler_function()

    # give user menu and option
    while True:
        # print menu and get input
        user_input = show_menu(expression_format)
        # run function based on input
        continue_curr_input = act_on_input(user_input, expression_format, expression)
        # continue with same input or new input by breaking loop
        if not continue_curr_input:
            break
    print("\n\n\t===============================================")                 
    print("\t================== NEW INPUT ==================")
    print("\t===============================================\n\n")

print("\n\n\n")