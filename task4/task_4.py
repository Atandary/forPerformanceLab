import math

path_to_array = input("Введите путь до файла: ")
array_nums = []
count = 0

with open(path_to_array) as f:
    for line in f:
        array_nums.append(int(line))

array_median = math.ceil((max(array_nums))/2)

for index, value in enumerate(array_nums):
    while value != array_median:
        if value < array_median:
            value += 1
        elif value > array_median:
            value -= 1
        count += 1
    else:
        array_nums[index] = value

print(count)