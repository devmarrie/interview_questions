# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

def isValid(s: str) -> bool:
        stack = []
        opens = {')': '(', '}': '{', ']':'['}

        for c in s:
            if c in opens: # if it is a closing bracket
                if stack and opens[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # add the opening bracket to the stack
        return True if not stack else False