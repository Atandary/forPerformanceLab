import math

path_to_circ = input("Введите путь до координат окружности: ")
path_to_dot = input("Введите путь до координат точек: ")

def get_coordinates(path_to_file):
    array_coordinates = []
    with open(path_to_file) as f:
        for line in f:
            array_coordinates.append([int(x) for x in line.split()])
    return array_coordinates

data_circ = get_coordinates(path_to_circ)
data_dot = get_coordinates(path_to_dot)

def check_point_position(x, y, radius = data_circ[1][0]):
    distance = math.sqrt((x - data_circ[0][0])**2 + (y - data_circ[0][1])**2)
    
    if distance < radius:
        return 1
    elif distance == radius:
        return 0
    else:
        return 2

for x, y in data_dot:
    result = check_point_position(x, y)
    print(result)
