import itertools
import string

def guess_password():
    chars = string.ascii_lowercase + string.digits
    for password_length in range(1, 9):
