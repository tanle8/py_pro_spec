"""
Link to the assignment:

"""

import sys


def draw_ladr():
    height = int(sys.argv[1])
    
    # Guaramteed only integers larger than 0 are fed to input
    if height <= 0:
        print ("Input must larger than 0")

    for num in range(1, height+1):
        # print(num)
        print('#'*num)
    

if __name__ == "__main__":
    draw_ladr()