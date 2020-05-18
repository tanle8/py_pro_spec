"""

"""



import sys

def sum_of_digit():
    # Split input string into character and convert elements to int
    digit_string = [int(x) for x in list(sys.argv[1])]
        
    return sum(digit_string)

if __name__ == "__main__":
    print(sum_of_digit())
