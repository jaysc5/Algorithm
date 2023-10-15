class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic_p = dict()
        s = list(s.split(' '))
        if len(s) != len(pattern):
            return False
        for i, p in enumerate(pattern):
            if p not in dic_p:
                dic_p[p] = s[i]
            else:
                if dic_p[p] != s[i]:
                    return False
        if len(set(dic_p.values())) != len(dic_p.values()):
            return False
        return True

            