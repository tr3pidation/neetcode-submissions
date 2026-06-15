class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # return False
        # above is nlog(n)

        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        for i in range(len(s)):
            hash_s[s[i]] += 1
        for i in range(len(t)):
            hash_t[t[i]] += 1
        return hash_s == hash_t

        
        
        
        