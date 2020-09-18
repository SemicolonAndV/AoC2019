# Part One

with open('input.txt', 'r') as file:
    result = [int(line) // 3 - 2 for line in file]

result_one = sum(result)

print(result_one)

# Part Two

additional_fuel = 0
for module in result:
    while module > 0:
        additional_fuel += module
        module = module // 3 - 2

result_two = additional_fuel

print(result_two)