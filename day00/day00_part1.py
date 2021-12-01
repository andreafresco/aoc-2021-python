# 
# Solution to Advent of Code 2021: day 00 part 1
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://adventofcode.com/
# 

def count_increment(file = r'./input.txt'):
    
    count = 0
    with open(file, 'r') as f:
        
        previous = int(f.readline().rstrip("\n"))
        print(previous)
        
        for line in f:
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