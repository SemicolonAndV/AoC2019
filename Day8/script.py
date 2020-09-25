import numpy as np

width, height, layers = 25, 6, 100
data = []
with open('input.txt') as file:
    for digit in file:
        for i in digit:
            if i == '\n':
                break
            data.append(int(i))

pre_image = np.reshape(data, [layers, height, width])
post_image = np.empty((height, width))
post_image.fill(2)
current_zero, current_one, current_two = 0, 0, 0
min_zero, min_one, min_two = 100, 0, 0

for x in range(layers):
    current_zero, current_one, current_two = 0, 0, 0
    for i in range(height):
        for j in range(width):
            current = pre_image[x, i, j]
            check = post_image[i, j]
            if check == 2 and current != 2:
                post_image[i, j] = current
            if current == 0:
                current_zero += 1

            elif current == 1:
                current_one += 1
            elif current == 2:
                current_two += 1
    if current_zero < min_zero:
        min_zero = current_zero
        min_one = current_one
        min_two = current_two

for h in range(0, height):
    for w in range(0, width):
        if post_image[h, w] == 0:
            print('  ', end='')
        else:
            print('X ', end='')
    print()
print("Result 1: ", min_one * min_two)