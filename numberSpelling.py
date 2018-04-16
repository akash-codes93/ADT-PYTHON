# code to convert number to string
# eg. 100 to One hundred

scale = ['', '', 'hundred ', 'thousand ', 'thousands ', 'lakhs ', 'lakh ', 'crore ', 'crores ']


def single(number):
    ones = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ', 'eleven ',
            'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']

    return ones[number]


def dual(number):
    _list = list(str(number))

    twos_prefix = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if number < 21:
        return single(number)
    else:
        output = twos_prefix[int(_list[0])] + " " + single(int(_list[1]))
        return output


def generalized(number, start, end):
    try:
        _scale = scale[len(str(number))-1]
    except IndexError:
        _scale = scale[-1]
    rem = int(str(number)[-start:])
    st = int(str(number)[-end::-1][::-1])

    output = get_string(st) + _scale + get_string(rem)

    return output


def get_string(number):
    zeros = len(str(number))-1

    if zeros == 0:
        return single(number)

    elif zeros == 1:
        return dual(number)

    elif zeros == 2:
        return generalized(number, start=2, end=3)

    elif zeros == 3 or zeros == 4:
        return generalized(number, start=3, end=4)

    elif zeros == 5 or zeros == 6:
        return generalized(number, start=5, end=6)

    else:
        return generalized(number, start=7, end=8)


if __name__ == '__main__':
    while 1:
        n = int(input("Enter a number:"))
        if n > 0:
            if len(n) > 14:
                raise ValueError('Hire Someone for this')
            print(get_string(n))
        else:
            raise StopIteration
