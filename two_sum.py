<<<<<<< HEAD
class Solutions:
    def twosum(self,nums, target):
        prevMap = {}
        for i,n in enumerate[nums]:
=======
class Solution:
    def twosum(self, nums, target):
        Hash = {}
        for i, n in enumerate [nums]:
>>>>>>> 8fa8685 (fixed)
            diff = target - n
            if diff in Hash:
                return(Hash[diff], i)
            Hash[n] = i
        return    