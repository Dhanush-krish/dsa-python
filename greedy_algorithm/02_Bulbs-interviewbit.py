#   https://www.interviewbit.com/problems/interview-questions/

class Solution:
    def bulbs(self, A):
        flips = 0
        
        for val in A:
            if flips %2 == 0:
                new = val
            else:
                new = not val
            
            if new == 1:
                continue
            else:
                flips += 1
        
        return flips
                
                
    


if __name__ == '__main__':
    obj = Solution()
    A = [0,1,0,1]
    ans = obj.bulbs(A)
    print(ans) 
