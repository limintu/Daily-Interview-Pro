class Solution:
    def calculate(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        s = s.replace(" ", "")

        stack = []
        signed = 1
        num = 0
        sum = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            else:
                if c == "+":
                    sum += signed * num
                    signed = 1
                    num = 0
                if c == "-":
                    sum += signed * num
                    signed = -1
                    num = 0
                if c == "(":
                    stack.append(sum)
                    stack.append(signed)
                    signed = 1
                    sum = 0
                if c == ")":
                    sum += signed * num
                    num = 0
                    sum = sum * stack.pop()
                    sum += stack.pop()

        if num != 0:
            sum += signed * num
        return sum
