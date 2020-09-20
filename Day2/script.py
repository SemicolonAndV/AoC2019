# PART ONE
with open('input.txt', 'r') as file:
    input = file.read().split(',')

opcodes = [int(x) for x in input]
opcodes[1] = 12
opcodes[2] = 2
pos = 0
while pos <= len(opcodes):
    if opcodes[pos] == 99:
        break
    elif opcodes[pos] == 1:
        opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] + opcodes[opcodes[pos + 2]]
    elif opcodes[pos] == 2:
        opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] * opcodes[opcodes[pos + 2]]
    pos += 4
print(opcodes[0])

# PART TWO

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
        if opcodes[0] == 19690720:
            result = 100 * noun + verb
            break

print(result)
