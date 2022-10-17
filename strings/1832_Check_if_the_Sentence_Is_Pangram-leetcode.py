# https://leetcode.com/problems/check-if-the-sentence-is-pangram/


# TC => O(n)
# SC => O(1)


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lookup = [0]*26

        for val in sentence:
            lookup[ord(val) - 97] = 1
        
        return sum(lookup) == 26


if __name__ == "__main__":
    obj = Solution()
    # sentence = "thequickbrownfoxjumpsoverthelazydog"
    sentence = "leetcode"
    ans = obj.checkIfPangram(sentence)
    print(ans)