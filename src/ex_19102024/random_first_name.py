import random
import string


def generate_random_first_name():
    first_name_length = random.randint(5, 10)
    first_name = ''.join(random.choices(string.ascii_letters, k=first_name_length))
    return first_name


for i in range(5):
    print(generate_random_first_name())

