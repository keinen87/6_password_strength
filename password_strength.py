import getpass
import string

blacklist = ['12345', 'qwerty', 'qwaszx', '1q2w3e']


def get_password_strength(password):
    score = 0
    if password in blacklist or len(password) < 5:
        return score
    has_lowercase_symbols = any(symbol in string.ascii_lowercase
                                for symbol in password)
    has_uppercase_symbols = any(symbol in string.ascii_uppercase
                                for symbol in password)
    has_digit_symbols = any(symbol in string.digits
                            for symbol in password)
    has_special_symbols = any(symbol in string.punctuation
                              for symbol in password)
    score = sum([has_lowercase_symbols, has_uppercase_symbols,
                 has_digit_symbols, has_special_symbols]) * 2.5
    if 5 <= len(password) < 8:
        score -= 2
        return score
    else:
        return score


if __name__ == '__main__':
    password = getpass.getpass()
    print('Password strength: {0}'.format(
        str(get_password_strength(password))))
