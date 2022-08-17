import itertools
import string

def guess_password():
    chars = string.ascii_lowercase + string.digits
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            with open("password.txt", "a") as f:
                guess = ''.join(guess)
                f.write(guess)
                f.write("\n")
guess_password()
