class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # brute force
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # return False
        # above is nlog(n)

        #two hashmaps
        # hash_s = defaultdict(int)
        # hash_t = defaultdict(int)
        # for i in range(len(s)):
        #     hash_s[s[i]] += 1
        # for i in range(len(t)):
        #     hash_t[t[i]] += 1
        # return hash_s == hash_t
        
        #one hashmap
        hash_s = defaultdict(int)
        for i in range(len(s)):
            hash_s[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in hash_s:
                return False
            else:
                hash_s[t[j]] -= 1
        for value in hash_s.values():
            if value != 0:
                return False
        return True


        
        
        
        