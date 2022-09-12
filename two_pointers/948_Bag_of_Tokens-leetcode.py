#   https://leetcode.com/problems/bag-of-tokens/


# T.C =>
# S.C =>


from typing import *


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        length, result, score = len(tokens), 0, 0
        tokens.sort()
        left, right = 0, length - 1

        while left <= right:

            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                result = max(result, score)
                left += 1
            elif score:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
        return result


if __name__ == "__main__":
    obj = Solution()
    tokens = [100, 200, 300, 400]
    power = 200
    ans = obj.bagOfTokensScore(tokens, power)
    print(ans)
