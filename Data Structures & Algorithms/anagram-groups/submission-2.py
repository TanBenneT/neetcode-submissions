class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        """
        Mapping char_count to list of str(anagrams)
        defaultdict(list) so that a missing key automatically starts as an empty list
        Without it you would need an "if key not in res" check before every append.
        """

        for s in strs:
            count = [0] * 26 # makes a fresh array of 26 zeros rep a to z, reset every after every loop

            for c in s: # walks through each char in string
                count[ord(c) - ord("a")] += 1 # turns a letter into an index and increments it in array.
                """
                ord() returns the integer unicode value
                ord("e") - ord("a") = 4, so e goes in index 4 in fresh array
                Lists can't be dictionary keys because they are mutable, so tuple(count) converts the array
                into something hashable. "eat" and "tea" both produce the same tuple (a1 e1 t1), so both go
                into the same list
                """
            res[tuple(count)].append(s) # ex. a1c1t1: ["act", "cat"]

        return list(res.values())