import sys
import math


def quad():
    a = int(sys.argv[1]) 
    b = int(sys.argv[2]) 
    c = int(sys.argv[3])

    # Calculate the discriminant
    d = (b**2) - (4*a*c)

    # Find two solutions
    x1 = int((-b - math.sqrt(d))/(2*a))
    x2 = int((-b + math.sqrt(d))/(2*a))

    print(f'{x1} \n {x2}')


if __name__ == "__main__":
    quad()