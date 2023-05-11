# My Answer
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_dic = {}
        for i in range(len(s)):
            if s[i] not in iso_dic:
                if t[i] not in iso_dic.values():
                    iso_dic[s[i]] = t[i]
                else:
                    return False
            else:
                if iso_dic[s[i]] != t[i]:
                    return False
        return True
    
# Better Solution
class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False