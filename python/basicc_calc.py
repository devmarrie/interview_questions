# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1 + 1"
# Output: 2

# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23


def calculate(s: str) -> int:
        output = 0
        curr = 0
        stack = []
        sign = 1
        
        for d in s:
            if d.isdigit():
                curr = curr*10 + int(d)
            elif d in "+-":
                output += (curr*sign)
                curr = 0
                if d == "-":
                    sign = -1
                else:
                    sign = 1
            elif d == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif d == ")":
                output += (curr*sign)
                output *= stack.pop()
                output += stack.pop()
                curr = 0
        return output + (curr*sign)