# 
# Solution to Advent of Code 2021: day 01 part 2
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://adventofcode.com/
# 

def count_increment_3_sliding(file):
    
    count = 0
    with open(file, 'r') as f:
        
        sliding_sum_n_1 = 0 # SUM[n-1]: previous value of the sliding sum
        sliding_sum_n = 0 # SUM[n]: actual value of the sliding sum
        x_n_3 = int(f.readline().rstrip("\n")) # x[n-3]: read the first value in the .txt file
        x_n_2 = int(f.readline().rstrip("\n")) # x[n-2]: read the second value in the .txt file
        x_n_1 = int(f.readline().rstrip("\n")) # x[n-1]: read the third value in the .txt file
        
        for line in f: # it starts from the fourth line of the .txt file
            str_num = line.rstrip("\n")
            if str_num: # avoid empty string (e.g. '')
                x_n = int(str_num) # convert string to integer
                
                sliding_sum_n_1 = x_n_1 + x_n_2 + x_n_3 # SUM[n-1] = x[n-1] + x[n-2] + x[n-3]
                sliding_sum_n = x_n + x_n_1 + x_n_2 # SUM[n] = x[n] + x[n-1] + x[n-2]
                
                if sliding_sum_n > sliding_sum_n_1:
                    count += 1
                
                sliding_sum_n_1 = 0 # previous value of the sliding sum
                sliding_sum_n = 0 # actual value of the sliding sum
                
                # moving the window
                x_n_3 = x_n_2
                x_n_2 = x_n_1
                x_n_1 = x_n
                  
    return count


if __name__ == "__main__":
    
    print(count_increment_3_sliding(file = r'./input.txt'))