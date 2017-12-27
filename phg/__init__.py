import random
import string
# https://docs.python.org/3/library/random.html#random.SystemRandom
choice = random.SystemRandom().choice

DEFAULT_LENGTH = 16


# http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html#password-policy-details
symbols = "!@#$%^&*()_+-=[]{}|'"


def random_password(length=DEFAULT_LENGTH, with_quote=False, symbol=True):
    '''
    Generate random password - NOT CRYPTOGRAPHICALLY SAFE
    (see Python3.6 secret module).

    symbol: use AWS symbol characters instead of punctuations (some char diff).
    with_quote: password might contain quotes
    '''
    punc = string.punctuation
    if symbol:
        punc = symbols

    if not with_quote:
        punc = punc.replace('"', '').replace("'", "")

    result = []
    result.append(choice(string.ascii_lowercase))
    result.append(choice(string.ascii_uppercase))
    result.append(choice(string.digits))
    result.append(choice(punc))
    for i in range(length - len(result)):
        result.append(choice(
            string.ascii_letters +
            string.digits + punc))
    random.shuffle(result)
    return ''.join(result)
