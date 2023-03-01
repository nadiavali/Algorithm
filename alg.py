'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.'''

class Solution(object):
    def search(self, nums, target):
        self.nums = nums
        self.target = target
        if self.target in self.nums:
            return self.nums.index(self.target)
        else:
            return -1