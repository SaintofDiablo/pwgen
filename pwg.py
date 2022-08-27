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
    pwg_length = len(pwg)
    if pwg_length < 8:
        print("Password:","".join(pwg))
        print("You have a weak password \n", "Recommendation is 8 characters")
        generate_random_pwg()
    else:
        print("Password:","".join(pwg))

generate_random_pwg()



