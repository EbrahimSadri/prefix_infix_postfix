# prefix_infix_postfix
Converts between prefix, infix and postfix expressions and evaluates them

</br>

## How to Use
- Pretty striaght forawrd, you don't need any libraries or any dependancies (I think, LOL). 
- Just have all the files in a single directory
- and just RUN **main.py**
```python main.py```

</br>

## Conversion
The coversion is done through 3 functions
 - prefix expression to postfix expression
 - postfix expression to infix expression
 - infix expression to prefix expression
 
Prefix -> Postfix -> Infix -> Prefix

### prefix expression to postfix expression
 1. Recursively loops through expression which is converted to a list using ```.split()``` based on spaces
 2. Looks for an element which is an operator followed by two consecutive elements which are operands
 3. Swaps elements around so that operator is at the end from "+ A B" to "A B +"
 4. Swaped segment is merged to beomce a single list element
 5. setps 1 - 4 are repeated until the list becomes a single element
 
### postfix expression to infix expression
 - Passes throught the expression left to right
 - if the character is an alphabet or a number: 
    - appended to operand list
 - else if character is an operator: 
    - then takes the last 2 elements in the operand list and combines with operator and bracets
    - saves it in a temporary variable and then pops the last two elements in the list
    - then appends the temporary variable into the operand list and resets temporary variable
    - eg: 
      - list = [ ... , A, B], character = + 
      - temp = ( A + B ), list = [ ... ]
      - list = [ ... , ( A + B ) ], temp = ""
 
### infix expression to prefix expression
just refer to this [youtube video](https://www.youtube.com/watch?v=8QxlrRws9OI)


</br>
</br>


## Evaluation
Evaluation is done through using ```eval()``` on an infix expression. 
So any expression is first converted to an infix expression then evaluated.


</br>
</br>

## Files
The files, for the most part are pretty self explanatory: 
- **input_handler.py** handles inputs
- **evaluation_handler.py** handles evaluation
- **conversion_handler.py** handles conversions between formats
- **menu_handler.py** handles the menu that is displayed in the console that asks user to choose what to do
- **constants.py** is basically 1 dictionary for operators and their precedence and 1 list for the different expression types
- **main.py** this is the one you want to run

</br>

## Disclaimer
- If a valid input is entered then the code will work as intended
- However it has not been made to be able to handle all types of inputs
- So you can probably break it by entering invalid inputs


</br></br>
But hey, knock yourself out with the code and Enjoy 😏
