import string
import sys


def get_password_strength(password):
    blacklist = ['qwerty','12345','123456','Password1','qwaszx','1q2w3e4r']
    score = 0
    low_cs_let, up_cs_let, num_dig, spec_char = False, False, False, False
    if password in blacklist:
        score += 1
        return score
    if password.isdigit():
        score += 2.5
        return score
    content = { 'low_cs_let': True for symbol in password if symbol in string.ascii_lowercase and not low_cs_let }
    content.update({'up_cs_let': True for symbol in password if symbol in string.ascii_uppercase and not up_cs_let })
    content.update({'num_dig': True for symbol in password if symbol in string.digits and not num_dig })
    content.update({'spec_char': True for symbol in password if symbol in string.punctuation and not spec_char })
    score = 2.5 * len(content.values())
    return score


if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print('Password strength: ' + str(get_password_strength(password)))
    else:
        print('Error! Enter password!')
