import random


def python_assignment_02_q1():
    length = 5
    numbers = []

    # get input
    while len(numbers) != length:
        while True:
            line = input('Enter a number: ')
            try:
                numbers.append(float(line))
                break
            except:
                print('Entered value is NOT valid! Try again...')

    # sort list
    numbers.sort()

    # calc sum of 2nd-max and 3rd-min, and mean
    n1 = numbers[len(numbers) - 2] + numbers[2]
    n2 = sum(numbers) / len(numbers)

    # show result
    print(numbers)
    print(f'sum of 2nd-max and 3rd-min : {n1}')
    print(f'mean : {n2}')
    print(n1 > n2)


def python_assignment_02_q2():
    word = 'P@#yn26at^&i5ve'

    # Pre-Processing
    word = word.lower()

    # ASCII values of characters are: [97 , 122]
    characters = 0
    # ASCII values of numbers are: [48 , 57]
    numbers = 0
    # ASCII values of special_characters are: All ascii code - (numbers+characters)
    special_characters = 0

    for item in word:
        if 97 <= ord(item) <= 122:
            characters += 1
        elif 48 <= ord(item) <= 57:
            numbers += 1
        else:
            special_characters += 1

    print(f'characters count: {characters}')
    print(f'numbers count: {numbers}')
    print(f'special characters count: {special_characters}')


def print_list_order(lst):
    count = 0
    for i in lst:
        count += 1
        print(f'{count} -> {i}')


def custom_comparator(gholam, ghamar):
    if len(gholam) > len(ghamar):
        lower = ghamar
    else:
        lower = gholam

    for i in range(0, len(lower)):
        if gholam[i] > ghamar[i]:
            return 1
        elif gholam[i] < ghamar[i]:
            return -1

    return 0


def python_assignment_02_q3():
    list_of_valid_chars = ['آ', 'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ',
                           'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط',
                           'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن',
                           'و', 'ه', 'ی', 'ئ', ' ']

    # list_of_valid_chars_ascii_code = []

    # for i in list_of_valid_chars:
    #     list_of_valid_chars_ascii_code.append(ord(i))

    list_of_words = []

    while True:
        line = input('Enter a persian word, please: ')
        is_valid = True

        for i in line:
            if i not in list_of_valid_chars:
                is_valid = False
                break

        if is_valid:
            list_of_words.append(line)
        else:
            print('Invalid char find! Try another word...')
            continue

        add = input('Thank you, do you want to add another word(y/n)? ')
        if add.lower() == 'n' or add.lower() == 'no':
            break

    from functools import cmp_to_key

    list_of_words.sort(
        key=cmp_to_key(
            custom_comparator
        )
    )
    print_list_order(list_of_words)


def python_assignment_02_q4():
    lst = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    for i in lst:
        if type(i) != str or len(i) == 0:
            lst.remove(i)

    print(lst)


def python_assignment_02_q5(length):
    if length < 8:
        print('Really? is it possible? Don\'t kidding!')

    # init
    password = ''
    valid_chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz',
                   '0123456789', '~!@#$%^&*{}[]().']
    upper = False
    lower = False
    num = False

    while len(password) < length:
        tmp = random.choice(valid_chars)
        char = random.choice(tmp)

        if char in valid_chars[0]:
            upper = True
        elif char in valid_chars[1]:
            lower = True
        elif char in valid_chars[2]:
            num = True

        password += char

        if len(password) == length:
            if not upper or not lower or not num:
                password = ''

    return password


def python_assignment_02_q6():
    while True:
        line = input('Enter an integer number: ')
        try:
            num = int(line)
            break
        except:
            print('Entered value is NOT valid!...')

    print(str(num) == str(num)[::-1])


def python_assignment_02_q7(lst):
    print(f'Original List: {lst}')
    tmp = []
    length = len(lst)
    while len(tmp) != length:
        choiced = random.choice(lst)
        tmp.append(choiced)
        lst.remove(choiced)

    print(f'Ordered List: {tmp}')


'''
0 -> first/last line
1 -> middle lines
'''


def repaire(line, order):
    start = '[0 '
    end = ' 0]'
    new_line = '\n'

    if order == 0:
        tmp = ''
        for i in range(len(line.split(' '))):
            tmp += '0 '
        return start + tmp.strip() + end + new_line
    elif order == 1:
        return start + line[1:len(line) - 1] + end + new_line


def python_assignment_02_q8():
    print('Start a line by [')
    print('End a line by ]')
    print('End of input by --')

    eof = '--'
    result = ''
    base = ''

    while True:
        line = input()
        if len(result) == 0:
            base = line
            result += repaire(line, 0)
            result += repaire(line, 1)
        elif line == eof:
            result += repaire(base, 0)
            break
        else:
            result += repaire(line, 1)

    print(result)


def python_assignment_02_q9(line):
    list_of_words = line.split()
    important = {}

    for item in list_of_words:
        important[item] = list_of_words.count(item)

    sort_words = sorted(important.items(), key=lambda x: x[1], reverse=True)

    for item in sort_words:
        if item[1] > 1:
            print(f'word: {item[0]} -> importance: {item[1]}')


def python_assignment_02_q10():
    pass


if __name__ == '__main__':
    # python_assignment_02_q1()
    # python_assignment_02_q2()
    # python_assignment_02_q3()
    # python_assignment_02_q4()
    # print(python_assignment_02_q5(16))
    # python_assignment_02_q6()
    # python_assignment_02_q7([2, 4, -1, 0, 33, 2, 1])
    # python_assignment_02_q8()
    python_assignment_02_q9('دیتا هاب یک دوره باحال ساخته که هاب هاب آدم رو درمیاره')
    # python_assignment_02_q10()
