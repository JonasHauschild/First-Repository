class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        liste = []
        if n == 2:
            if nums[0] + nums[1] == target:
                if nums[0] == nums[1]:
                    liste.append(0)
                    liste.append(1)
                else:
                    liste.append(nums.index(nums[0]))
                    liste.append(nums.index(nums[1]))
        else:
            for i in range(0, n):
                for j in range(1, n):
                    summe = nums[i]+ nums[j]
                    if summe == target:
                        liste.append(nums.index(nums[j]))
                        liste.append(nums.index(nums[i]))
                        break
                    break
        return liste

n = [2,7,11,15]
t = 9

a = Solution() #a ist ein Objekt der Klasse Solution

print(a.twoSum(n,t))

