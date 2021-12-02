# 
# Solution to Advent of Code 2021: day 02 part 2
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://adventofcode.com/
# 

def dive_depth_position_aim(input_file):
    
    h_position = 0 # initialize horizontal position
    depth = 0 # initialize depth
    aim = 0 # initialize aim
    
    with open(input_file, 'r') as f:
        for line in f:
            command, x = line.split() # command = {forward, down, up}, x: integer value
            
            if command == 'forward':
                h_position += int(x)
                depth += aim * int(x)
            elif command == 'up': 
                aim -= int(x)
            elif command == 'down': 
                aim += int(x)
            else:
                print(f"Command {command} not recognized")
                return -1

    return depth*h_position


if __name__ == "__main__":
    
    print(dive_depth_position_aim(input_file=r'./input.txt'))