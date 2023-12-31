from task_1 import beam_simulator


def main():
    with open('input.txt', 'r') as file:
        contraption = [line.replace('\\', '7').strip() for line in file]

    starting_pos_dir = []
    for x in range(len(contraption[0])):
        for y in range(len(contraption)):
            if x == 0:
                starting_pos_dir.append(((y, x - 1), 'r'))
            elif y == 0:
                starting_pos_dir.append(((y - 1, x), 'd'))
            elif x == len(contraption[0]) - 1:
                starting_pos_dir.append(((y, x + 1), 'l'))
            elif y == len(contraption) - 1:
                starting_pos_dir.append(((y + 1, x), 'u'))

    print(max([beam_simulator(pos, direction, contraption) for pos, direction in starting_pos_dir]))


if __name__ == '__main__':
    main()
