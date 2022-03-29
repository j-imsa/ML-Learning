def repair_line_in_step_one(line, width):
    space = ' '
    if len(line) == width : return line
    result = line
    while len(result) <= width:
        result = space + result
    return result


def repair_line_in_step_two(line, width, row):
    space = ' '
    if len(line) == width: return line
    result = line[::-1].strip()
    if row >= 1 :
        result = width*space + result
    return result


def print_star():
    chars = ['*', '#', '$']
    space = ' '
    new_line = '\n'
    result = ''
    height = 3
    width = 5


    # step 01:
    for i in range(1, height+1):
        line = ''
        for j in range(i):
            line += chars[j]
            line += space
        line = repair_line_in_step_one(line, width) + new_line
        result += line

    # step 02: remove \n and $
    result = result[:len(result)-2]

    # step 03:
    for i in range(1, height+1)[::-1]:
        line = ''
        for j in range(i):
            line += chars[j]
            line += space
        line = repair_line_in_step_two(line, width, height-i) + new_line
        result += line[1:]

    print(result)


if __name__ == '__main__':
    print_star()
