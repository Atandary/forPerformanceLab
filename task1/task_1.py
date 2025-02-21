import sys

array_len = int(sys.argv[1])
interval = int(sys.argv[2])

array_circ = interval * [int(i) for i in range(1, array_len + 1)]

array_temp = [""]
array_solution = []
count = 0

while array_temp[-1] != 1:
    array_temp.clear()

    for k in range(count, interval + count):
        array_temp.append(array_circ[k])
        count += 1 

    array_solution.append(array_temp.copy())
    count -= 1

for j in range(len(array_solution)):
    print(array_solution[j][0], end='')




