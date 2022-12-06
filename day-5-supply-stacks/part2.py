from collections import deque

stacks = {
    1: deque(),
    2: deque(),
    3: deque(),
    4: deque(),
    5: deque(),
    6: deque(),
    7: deque(),
    8: deque(),
    9: deque(),
}

with open("day-5-supply-stacks/input.txt") as f:
    for line_num, line in enumerate(f, start=1):

        # create initial supply stacks
        if line_num < 9:
            lines = [1, 5, 9, 13, 17, 21, 25, 29, 33]
            for i, l in enumerate(lines, start=1):
                if line[l] != " ":
                    stacks[i].appendleft(line[l])

        # parse and execute procedures
        if line_num > 10:
            procedure = line.strip().split()
            amount = int(procedure[1])
            from_stack = int(procedure[3])
            to_stack = int(procedure[5])

            crates = reversed([stacks[from_stack].pop() for _ in range(amount)])
            stacks[to_stack].extend(crates)

print(
    (
        f"{stacks[1][-1]}{stacks[2][-1]}{stacks[3][-1]}{stacks[4][-1]}{stacks[5][-1]}"
        f"{stacks[6][-1]}{stacks[7][-1]}{stacks[8][-1]}{stacks[9][-1]}"
    )
)
