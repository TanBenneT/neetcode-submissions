class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping char_count to list of str(anagrams)

        for s in strs:
            count = [0] * 26 # a - z

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord() returns the integer unicode value
            
            res[tuple(count)].append(s)

            """
            A tuple is hashable, so it can be used as a dictionary key. Lists cannot be dictionary keys because they are mutable.
            """

        return list(res.values())