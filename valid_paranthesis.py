#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string 
#is valid if:
#1.Open brackets must be closed by the same type of brackets.
#2.Open brackets must be closed in the correct order.
#3.Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        # use stack to store open paranthesis
        stack = []
        # use dictionary to compare open paranthesis that are popped to 
        # close paranthesis in string after exausting open paranthesis
        dict = {"(":")","[":"]","{":"}"}

        for char in s:
            if char in dict:
                stack.append(char)
            elif not stack or dict[stack.pop()] != char:
                return False
            
        return len(stack) == 0