import random

def pick(stream):
    random_el = None

    for i, e in enumerate(stream):
        if i == 0:
            random_el = e
        elif random.randint(1, i+1) == 1:
            random_el = e
        
    return random_el

print(pick([1,2,3,5,6,8,7]))