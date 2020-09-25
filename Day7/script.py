from itertools import permutations
with open('input.txt', 'r') as file:
    input_data = file.read().split(',')


def intcode(data, input_seq):

    opcodes = [int(x) for x in data]
    input_pos = 0
    pos = 0
    output = 0
    param3 = opcodes[pos + 3]
    param2 = opcodes[pos + 2]
    param1 = opcodes[pos + 1]
    while pos + 3 < len(opcodes):
        check = opcodes[pos] + 10000
        param3 = opcodes[pos + 3]
        param2 = opcodes[pos + 2] if int(str(check)[1]) == 0 else pos + 2
        param1 = opcodes[pos + 1] if int(str(check)[2]) == 0 else pos + 1
        opcode = opcodes[pos] % 100
        if opcode == 1:
            opcodes[param3] = opcodes[param1] + opcodes[param2]
            pos += 4
        elif opcode == 2:
            opcodes[param3] = opcodes[param1] * opcodes[param2]
            pos += 4
        elif opcode == 3:
            if input_pos == 0:
                opcodes[param1] = input_seq[input_pos]
                input_pos += 1
            else:
                opcodes[param1] = input_seq[input_pos]
            pos += 2
        elif opcode == 4:
            output = opcodes[param1]
            pos += 2
        elif opcode == 5:
            if opcodes[param1] != 0:
                pos = opcodes[param2]
            else:
                pos += 3
        elif opcode == 6:
            if opcodes[param1] == 0:
                pos = opcodes[param2]
            else:
                pos += 3
        elif opcode == 7:
            opcodes[param3] = 1 if opcodes[param1] < opcodes[param2] else 0
            pos += 4
        elif opcode == 8:
            opcodes[param3] = 1 if opcodes[param1] == opcodes[param2] else 0
            pos += 4
        elif opcode == 99:
            return output


perm_list_1 = list(permutations(range(5)))
perm_list_2 = list(permutations(range(5, 10)))
max_output_1 = 0
for permutation in perm_list_1:
    output = 0
    for phase in permutation:
        output = intcode(input_data, [phase, output])
    if output > max_output_1:
        max_output_1 = output
print("Result 1: ", max_output_1)
