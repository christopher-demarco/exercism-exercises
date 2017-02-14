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
    pass


if __name__ == '__main__':
    encode('foobar')
