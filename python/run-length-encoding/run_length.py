def encode(string):
    encoding = '0'
    prev = string[0]
    for curr in string:
        if curr == prev:
            encoding = f'{encoding[:-1]}{str(int(encoding[-1])+1)}'
        else:
            encoding = f'{encoding}{prev}1'
        prev = curr
    encoding = f'{encoding}{curr}'
    return encoding


def decode(string):
    pass
