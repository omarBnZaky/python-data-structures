"""
Use a stack to check whether or not a string
has balanced usage of parnthesis.
"""

from stack import Stack


def is_match(p1,p2):
    print("math func:" + str((p1,p2)))
    if p1 == '(' and p2 == ')':
        print("match")
        return True
    elif p1 == '{' and p2 == '}':
        print("match")
        return True
    elif p1 == '[' and p2 == ']':
        print("match")
        return True
    else:
        print("never")
        return False
def is_paren_balanced(paren_string):    
    s = Stack()
    is_balanced = True
    index = 0
   # print(len(paren_string))
    while  index < len(paren_string) and is_balanced:
        print(index)
        paren = paren_string[index]
        if paren in '([{':
            s.push(paren)
        else: 
            if s.is_empty():
                is_balanced=False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False

        index+=1
    print("items :" +str(s.get_stack()))
    # return is_balanced

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced('[()]]'))

# elif s.is_empty() or not is_match(s.stack_top_element(),paren):
