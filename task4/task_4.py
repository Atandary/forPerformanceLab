import math
import sys

path_to_array = sys.argv[1]
array_nums = []

with open(path_to_array) as f:
    for line in f:
        array_nums.append(int(line))

array_len = len(array_nums)
array_nums.sort()

if array_len % 2 == 1: 
    array_median = array_nums[array_len // 2]
else:
    array_median = array_nums[array_len // 2 - 1]

count = sum(abs(num - array_median) for num in array_nums)


print(count)