class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        num = 0
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c) # 숫자가 연달아 들어올 경우 자릿 수 증가
                
            elif c.isalpha():
                currStr += c
                
            elif c == '[':
                stack.append((num, currStr))
                currStr = ""
                num = 0
                
            elif c == ']':
                pre_num, pre_str = stack.pop()
                currStr = pre_str + pre_num * currStr
        
        return currStr