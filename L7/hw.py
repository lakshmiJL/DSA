"""
Infix Expression: An infix expression is a mathematical expression where operators are written between operands. For example, "3 + 4 * 2" is an infix expression.

Postfix Expression (also known as Reverse Polish Notation or RPN): A postfix expression is a mathematical expression where operators are written after their operands. Using the same example as above, the postfix expression equivalent would be "3 4 2 * +".

The main advantage of postfix notation is that it eliminates the need for parentheses to indicate the order of operations. It also makes the evaluation of expressions more straightforward.

Operator Priorities (Precedence): In infix expressions, operators have different priorities or precedence. For example, multiplication and division usually have higher priority than addition and subtraction. This determines the order in which operations are performed. Parentheses can be used to override the default precedence.

Algorithm for Infix to Postfix Conversion:

To convert an infix expression to a postfix expression, we can use a stack to keep track of operators. Here's a step-by-step algorithm:

Initialize an empty stack for operators and an empty list for the output postfix expression.
Scan the infix expression from left to right.
If the current element is an operand (a number or a variable), add it to the output list.
If the current element is an operator, then:
a. Pop operators from the stack and add them to the output list until either the stack is empty or the operator at the top of the stack has lower precedence.
b. Push the current operator onto the stack.
If the current element is an opening parenthesis '(', push it onto the stack.
If the current element is a closing parenthesis ')', pop operators from the stack and add them to the output list until an opening parenthesis '(' is encountered. Pop and discard the '(' from the stack.
Once the input expression is fully scanned, pop any remaining operators from the stack and add them to the output list.
The final output list will contain the postfix expression.

Here's a simple example to illustrate the process:
Infix: 2 + 3 * 4
Postfix: 2 3 4 * +

Operator Precedence:

In general, operator precedence follows the standard rules of mathematics:

Parentheses
Exponents/Power
Multiplication and Division
Addition and Subtraction
Here's the pseudo code for the algorithm:


function infixToPostfix(infixExpression):
    initialize empty stack
    initialize empty list for postfix expression
    
    for each element in infixExpression:
        if element is an operand:
            add element to postfix expression
        else if element is an operator:
            while stack is not empty and precedence(stack.top()) >= precedence(element):
                add stack.pop() to postfix expression
            push element onto stack
        else if element is '(':
            push element onto stack
        else if element is ')':
            while stack.top() is not '(':
                add stack.pop() to postfix expression
            stack.pop() // Pop and discard '('
    
    while stack is not empty:
        add stack.pop() to postfix expression
    
    return postfix expression

"""
def infix_to_postfix(infix_expression):
    def precedence(operator):
        if operator in ['+', '-']:
            return 1
        if operator in ['*', '/']:
            return 2
        if operator in ['^']:
            return 3
        return 0

    def is_operator(char):
        return char in ['+', '-', '*', '/', '^']

    stack = []
    postfix_expression = []
    
    for element in infix_expression:
        if element.isalnum():  # Operand
            postfix_expression.append(element)
        elif is_operator(element):  # Operator
            while stack and is_operator(stack[-1]) and precedence(stack[-1]) >= precedence(element):
                postfix_expression.append(stack.pop())
            stack.append(element)
        elif element == '(':  # Opening parenthesis
            stack.append(element)
        elif element == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()  # Pop and discard '('

    while stack:
        postfix_expression.append(stack.pop())
    
    return ' '.join(postfix_expression)

infix_expression = "a + b * ( c ^ d - e ) ^ ( f + g * h ) - i "
postfix_result = infix_to_postfix(infix_expression.split())
print(postfix_result)
