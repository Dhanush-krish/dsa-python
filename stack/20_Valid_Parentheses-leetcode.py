#   https://leetcode.com/problems/valid-parentheses/



class Solution:
    def isValid(self, s: str) -> bool:
        check = {"}":"{", "]":"[", ")":"("}
        stack = []
        
        for element in s:
            if element in {"(", "[", "{"}:
                stack.append(element)
            elif stack and stack[-1] == check[element]:
                    stack.pop()
            else:
                return False
        
        return False if stack else True


if __name__ == '__main__':
    obj = Solution()
    s = "()[]{"
    ans = obj.isValid(s)
    print(ans)