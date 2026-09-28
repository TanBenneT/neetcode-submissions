class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        return sorted(s) == sorted(t) -- T: O(nlogn), S: O(1) / O(n) -> depends on built-in library

        return Counter(s) == Counter(t) -- Simplified using built-in function (Not accepeted in Interviews)
        """

        if len(s) != len(t): # Anagram Length needs to be same
            return False

        mapS, mapT = {}, {} # Creating Hashmap for both string S and T

        for i in range(len(s)): # Length of both s and t are same
            mapS[s[i]] = 1 + mapS.get(s[i], 0) # adds 1 to count, default 1 + 0 if not in map yet 
            mapT[t[i]] = 1 + mapT.get(t[i], 0) # adds 1 to count, default 1 + 0 if not in map yet 

        for c in mapS:
            if mapS[c] != mapT.get(c, 0): # checks count in hashmap for each letter if same
                return False

        return True
