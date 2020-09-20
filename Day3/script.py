# PART ONE
with open('input.txt', 'r') as file:
    A, B = file.read().split('\n')
    A, B = [x.split(',') for x in [A, B]]

# defining directions
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def get_points(wire):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in wire:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


PA = get_points(A)
PB = get_points(B)
both_wires = set(PA.keys()) & set(PB.keys())
result_1 = min([abs(x) + abs(y) for (x, y) in both_wires])
print("Part 1: ", result_1)
result_2 = min([PA[p] + PB[p] for p in both_wires])
print("Part 2: ", result_2)
