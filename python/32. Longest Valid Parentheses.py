class Solution:
    def longestValidParentheses(self, s: str) -> int:
        cnt, length = 0, 0
        stack = []

        for key in list(s):
            if key == "(":
                stack.append(key)
            else:
                if len(stack) > 0:
                    stack.pop()
                    cnt += 1
            if len(stack) == 0:
                cnt = 0
            length = max(length, cnt*2)

        return length

s = Solution()
str = "(()" # 2
print(s.longestValidParentheses(str))
str = ")()())" # 4
print(s.longestValidParentheses(str))
str = "()(()" # 2
print(s.longestValidParentheses(str))
str = ")()())" # 4
print(s.longestValidParentheses(str))