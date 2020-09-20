with open('input.txt', 'r') as file:
    input = file.read().split(',')

opcodes = [int(x) for x in input]

for noun in range(100):
    for verb in range(100):
        opcodes = [int(x) for x in input]
        opcodes[1] = noun
        opcodes[2] = verb
        pos = 0
        while pos <= len(opcodes):
            if opcodes[pos] == 99:
                break
            elif opcodes[pos] == 1:
                opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] + opcodes[opcodes[pos + 2]]
            elif opcodes[pos] == 2:
                opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] * opcodes[opcodes[pos + 2]]
            pos += 4
        if (noun, verb) == (12, 2):
            result_1 = opcodes[0]
        if opcodes[0] == 19690720:
            result_2 = 100 * noun + verb
            break

print("Result 1: ", result_1)
print("Result 2: ", result_2)
