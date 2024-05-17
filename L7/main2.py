#Given an expression string
#Write a python program to find whether a given string has balanced parentheses or not. 

#One approach to check balanced parentheses is to use stack. 
# Each time, when an open parentheses is encountered push it in the stack, 
# and when closed parenthesis is encountered, match it with the top of stack and pop it. 
# If stack is empty at the end, return Balanced otherwise, Unbalanced. 

open_list = ["[","{","("]
close_list = ["]","}",")"] 

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i) #stack = [{]
        elif i in close_list:
            pos = close_list.index(i) #pos = 1
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced" 
    else:
        return "Unbalanced"


# Driver code
string = "{Hello}"
print(string,"-", check(string))