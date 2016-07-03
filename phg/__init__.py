import random
import string


PUNC_NO_QUOTE = string.punctuation.replace('"', '').replace("'", "")
DEFAULT_LENGTH = 16


def random_password(length=DEFAULT_LENGTH, with_quote=False):
    punc = string.punctuation if with_quote else PUNC_NO_QUOTE

    result = []
    result.append(random.choice(string.ascii_lowercase))
    result.append(random.choice(string.ascii_uppercase))
    result.append(random.choice(string.digits))
    result.append(random.choice(punc))
    for i in range(length-len(result)):
        result.append(random.choice(
            string.ascii_letters +
            string.digits + punc))
    random.shuffle(result)
    return ''.join(result)
