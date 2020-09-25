def intcode(input_file, input_number):

    with open(input_file, 'r') as file:
        input_data = file.read().split(',')

    opcodes = [int(x) for x in input_data]

    pos = 0
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
            opcodes[param1] = input_number
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
            break
    return output


print("Result 1: ", intcode('input.txt', 1))
print("Result 2: ", intcode('input.txt', 5))