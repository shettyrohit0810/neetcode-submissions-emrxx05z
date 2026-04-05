class Solution:
    def isValid(self, s: str) -> bool:
        val = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in val:
                if stack and stack[-1] == val[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack