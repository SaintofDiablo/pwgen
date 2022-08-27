import random
import secrets
import string

characters = list(string.ascii_letters + string.digits + "!@#$^&*()%<>_+=-")
def generate_random_pwg():
    length = int(input("Enter password length:  "))
    random.shuffle(characters)
    pwg = []
    for i in range(length):
        pwg.append(secrets.choice(characters))
    random.shuffle(pwg)
    print("".join(pwg))
generate_random_pwg()



