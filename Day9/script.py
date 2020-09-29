with open('input.txt', 'r') as file:
    input_data = file.read().split(',')


def decode(num):
    digits = [0 for _ in range(5)]
    position = len(digits) - 1
    while num > 0 and position >= 0:
        digits[position] = num % 10
        num //= 10
        position -= 1
    return digits


def getmode(data, mode, current_position, offset, base):
    if mode == 0:
        return data[current_position + offset]
    if mode == 1:
        return current_position + offset
    if mode == 2:
        return data[current_position + offset] + base


def intcode(data, input_seq):

    opcodes = [0] * 100000
    for i, x in enumerate(data):
        opcodes[i] = int(x)
    pos = 0
    input_pos = 0
    output = 0
    relative_base = 0

    while True:
        param1 = decode(opcodes[pos])[2]
        param2 = decode(opcodes[pos])[1]
        param3 = decode(opcodes[pos])[0]
        opcode = decode(opcodes[pos])[3] * 10 + decode(opcodes[pos])[4]
        if opcode == 1:
            op1, op2, op3 = getmode(opcodes, param1, pos, 1, relative_base), \
                            getmode(opcodes, param2, pos, 2, relative_base), \
                            getmode(opcodes, param3, pos, 3, relative_base)
            opcodes[op3] = opcodes[op1] + opcodes[op2]
            pos += 4
        elif opcode == 2:
            op1, op2, op3 = getmode(opcodes, param1, pos, 1, relative_base), \
                            getmode(opcodes, param2, pos, 2, relative_base), \
                            getmode(opcodes, param3, pos, 3, relative_base)
            opcodes[op3] = opcodes[op1] * opcodes[op2]
            pos += 4
        elif opcode == 3:
            opcodes[getmode(opcodes, param1, pos, 1, relative_base)] = input_seq
            pos += 2
        elif opcode == 4:
            output = opcodes[getmode(opcodes, param1, pos, 1, relative_base)]
            pos += 2
        elif opcode == 5:
            op1, op2 = getmode(opcodes, param1, pos, 1, relative_base), \
                       getmode(opcodes, param2, pos, 2, relative_base)
            if opcodes[op1] != 0:
                pos = opcodes[op2]
            else:
                pos += 3
        elif opcode == 6:
            op1, op2 = getmode(opcodes, param1, pos, 1, relative_base), \
                       getmode(opcodes, param2, pos, 2, relative_base)
            if opcodes[op1] == 0:
                pos = opcodes[op2]
            else:
                pos += 3
        elif opcode == 7:
            op1, op2, op3 = getmode(opcodes, param1, pos, 1, relative_base), \
                            getmode(opcodes, param2, pos, 2, relative_base), \
                            getmode(opcodes, param3, pos, 3, relative_base)
            opcodes[op3] = 1 if opcodes[op1] < opcodes[op2] else 0
            pos += 4
        elif opcode == 8:
            op1, op2, op3 = getmode(opcodes, param1, pos, 1, relative_base), \
                            getmode(opcodes, param2, pos, 2, relative_base), \
                            getmode(opcodes, param3, pos, 3, relative_base)
            opcodes[op3] = 1 if opcodes[op1] == opcodes[op2] else 0
            pos += 4
        elif opcode == 9:
            relative_base += opcodes[getmode(opcodes, param1, pos, 1, relative_base)]
            pos += 2
        elif opcode == 99:
            return output


print('Result 1:', intcode(input_data, 1))
print('Result 2:', intcode(input_data, 2))