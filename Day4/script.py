with open('input.txt', 'r') as file:
    start, stop = file.read().split('-')

start = int(start)
stop = int(stop)
result_1 = 0
result_2 = 0

for pword in range(start, stop):
    isdouble = False
    num = [int(i) for i in str(pword)]
    if num == sorted(num):
        counts = {str(pword).count(x) for x in str(pword)}  # check how many times a digit shows up in a given number
        if any(num[i] == num[i + 1] for i in range(len(num) - 1)):  # check if any two adjacent digits are equal
            result_1 += 1
        if 2 in counts:  # check if two adjacent matching digits are not a part of a larger group of matching digits
            result_2 += 1

print("Result 1: ", result_1)
print("Result 2: ", result_2)
