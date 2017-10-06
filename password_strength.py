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
    content = { 'low_cs_let': True for symbol in password if 97 <= ord(symbol) <= 122 and not low_cs_let }
    content.update({'up_cs_let': True for symbol in password if 65 <= ord(symbol) <= 90 and not up_cs_let })
    content.update({'num_dig': True for symbol in password if 48 <= ord(symbol) <= 57 and not num_dig })
    content.update({'spec_char': True for symbol in password if (33 <= ord(symbol) <= 47 \
     or 58 <= ord(symbol) <= 64 or 91 <= ord(symbol) <= 96 or 123 <= ord(symbol) <= 126) and not spec_char })
    score = 2.5 * len(content.values())
    return score


if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print('Password strength: ' + str(get_password_strength(password)))
    else:
        print('Error! Enter password!')
