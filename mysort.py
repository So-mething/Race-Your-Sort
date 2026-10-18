def my_sort(nums):
  n = len(nums)
  for i in range(1, n):
    key, j = nums[i], i-1
    while j >= 0 and nums[j] > key:
      nums[j+1] = nums[j]
      j -=1
      nums[j+1] = key

nums = [5, 2, 4]
my_sort(nums)
print(*nums)
