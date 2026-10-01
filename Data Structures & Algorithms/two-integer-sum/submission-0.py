class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # val : index (Index = value as the output looks for index) (Val = Key)

        """
        target - n = 2nd pair of num for answer (diff)
        check if diff in our hashmap -> have we gone past it?
        if diff in hashmap, means we have our answer
        else add n to hashmap
        """

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i