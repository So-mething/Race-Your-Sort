def my_sort(nums):
  n = len(nums)
  for i in range(1, n):
  key, j = a[i], i-1
  while j >= 0 and a[j] > key:
    a[j+1] = a[j]
    j -=1
    a[j+1] = key

nums = [5, 2, 4]
my_sort(nums)
print(*nums)
