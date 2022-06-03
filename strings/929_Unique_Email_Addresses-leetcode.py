#   https://leetcode.com/problems/unique-email-addresses/

class Solution(object):
    
    def clean_email(self, email):
        local_name,domain = email.split('@')
        local_name = local_name.split('+')[0]
        local_name = local_name.replace('.','')
        return local_name+'@'+domain
        
    
    
    def numUniqueEmails(self, emails):
        distinct_email = set()
        
        for email in emails:
            distinct_email.add(self.clean_email(email))
        return len(distinct_email)


if __name__ == "__main__":
    obj = Solution()
    ip = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
        ]
    output = obj.numUniqueEmails(ip)
    print(output)
    