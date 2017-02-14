import re


def encode(string):

    def _encode(count, char):
        if count == 1:
            return char
        else:
            return f'{str(count)}{char}'
    encoded = ''
    prev = string[0]
    count = 0
    for curr in string:
        if curr == prev:
            count += 1
        else:
            encoded = f'{encoded}{_encode(count, prev)}'
            count = 1
        prev = curr

    encoded = f'{encoded}{_encode(count, prev)}'
    return encoded


def decode(string):
    original = ''
    atoms = []
    n = ''
    for x in string:
        if re.match('\d', x):
            n += x
        else:
            if n != '':
                atoms.append(n)
                n = ''
            atoms.append(x)
    atoms.reverse()
    while True:
        try:
            char = str(atoms.pop())
        except IndexError:
            break
        if re.match('\d+', char):
            count = int(char)
            char = atoms.pop()
            original += f'{char*count}'
        else:
            original += char
            continue
    return original


if __name__ == '__main__':
    encode('foobar')
