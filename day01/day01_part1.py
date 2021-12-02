# 
# Solution to Advent of Code 2021: day 01 part 1
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://adventofcode.com/
# 

def count_increment(file = r'./input.txt'):
    
    count = 0 # counting variable
    
    with open(file, 'r') as f: # open a file in reading mode
        
        previous = int(f.readline().rstrip("\n")) # read the first line
        
        for line in f: # it starts from the second line onwards
            str_num = line.rstrip("\n")
            if str_num: # avoid empty string (e.g. '')
                num = int(str_num) # convert string to integer
                #print(num)
                if num > previous:
                    count += 1
                
                previous = num
                  
    return count


if __name__ == "__main__":
    
    print(count_increment())