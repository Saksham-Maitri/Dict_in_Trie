import random

# a funton to generate a random string containing "a" to "z" of length 10 to 100
def random_string():
    length = random.randint(10, 100)
    return ''.join([chr(random.randint(97, 122)) for i in range(length)])
with open('input.txt', 'w') as f:
    for i in range(10000):
        f.write(str(i+1) + '\n')
        f.write(random_string() + '\n')
    f.write('0\n')

