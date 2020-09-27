from math import gcd, atan2, degrees
from collections import OrderedDict


def read_positions():
    with open('input.txt', 'r') as file:
        for y, line in enumerate(file.readlines()):
            for x, a in enumerate(line):
                if a == '#':
                    yield x, y


# Part 1
asteroids = list(read_positions())
max_visible = 0
visible_asteroids = []
best_asteroid = None
for rock_1 in asteroids:
    visible = set()
    for rock_2 in asteroids:
        if rock_1 != rock_2:
            dx, dy = rock_2[0] - rock_1[0], rock_2[1] - rock_1[1]
            dx, dy = dx // gcd(dx, dy), dy // gcd(dx, dy)
            visible.add((dx, dy))
    if len(visible) > max_visible:
        max_visible = len(visible)
        visible_asteroids = visible
        best_asteroid = rock_1

# Part 2
angles_list = {}
for vector in visible_asteroids:
    angles_list[vector] = ((degrees(atan2(vector[1], vector[0])) + 90) % 360)

sorted_angles = OrderedDict(sorted(angles_list.items(), key=lambda x: x[1]))
element_200 = (list(sorted_angles.items())[199][0])
result_2 = (element_200[0] + best_asteroid[0]) * 100 + element_200[1] + best_asteroid[1]

print("Result 1: ", max_visible, best_asteroid)
print("Result 2: ", result_2)
