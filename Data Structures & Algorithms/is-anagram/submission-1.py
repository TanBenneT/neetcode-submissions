class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        return sorted(s) == sorted(t) -- T: O(nlogn), S: O(1) / O(n) -> depends on built-in library

        return Counter(s) == Counter(t) -- Simplified using built-in function (Not accepeted in Interviews)
        """

        if len(s) != len(t):
            return False

        mapS, mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)

        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False

        return True
