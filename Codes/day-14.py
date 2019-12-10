import random

def MonteCarlo(n):
    circle_points = sqaure_points = 0
    pi = 0

    for _ in range(n):
        rand_x = random.random()
        rand_y = random.random()

        dist = rand_x**2 + rand_y**2

        if dist <= 1:
            circle_points += 1
        
        sqaure_points += 1

        pi = (4*circle_points)/sqaure_points
    
    return pi

print("{:,.3f}".format(MonteCarlo(10000)))

