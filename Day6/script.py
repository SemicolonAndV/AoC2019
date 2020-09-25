with open('input.txt', 'r') as file:
    data = file.read().split('\n')

orbit_list = {}
for connection in data:
    x, y = connection.split(')')
    orbit_list[y] = x

counter_1 = 0
you, san = [], []
for element in orbit_list.keys():
    current = element
    if current == 'YOU':
        list_you = True
    elif current == 'SAN':
        list_san = True
    else:
        list_you, list_san = False, False
    while current != 'COM':
        current = orbit_list[current]
        if list_you:
            you.append(current)
        if list_san:
            san.append(current)
        counter_1 += 1

print('Result 1: ', counter_1)
print('Result 2: ', len(set(you) ^ set(san)))