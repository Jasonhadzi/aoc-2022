#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv
import re

def read_csv(path):

    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile,delimiter=','))
    return data

def follow_instructions(instructions,starting_arrays):
    
    arrays = starting_arrays
    for order in instructions:
        split_order = re.split('move|from|to',order[0])
        #print(split_order)
        num_of_crates = int(split_order[1])
        #index starts at 0
        from_arr_index = int(split_order[2])-1
        to_arr_index = int(split_order[3])-1
        #print('move {} from {} to {}'.format(num_of_crates,from_arr_index,to_arr_index))
        
        #to move num_of_crates, we pop as many times as the number of crates
        # we pop from the array with index from_arr_index
        # we append to the array with index to_arr_index
        for x in range (num_of_crates): 
            array_to_pop = arrays[from_arr_index]
            arry_to_append = arrays[to_arr_index]
            
            arry_to_append = arry_to_append.append(array_to_pop.pop())

            #print('new status of arrays: {}'.format(arrays))
    return arrays

def follow_instructions_p2(instructions,starting_arrays):
    
    arrays = starting_arrays
    for order in instructions:
        split_order = re.split('move|from|to',order[0])
        #print(split_order)
        num_of_crates = int(split_order[1])
        #index starts at 0
        from_arr_index = int(split_order[2])-1
        to_arr_index = int(split_order[3])-1
        #print('move {} from {} to {}'.format(num_of_crates,from_arr_index,to_arr_index))
        
        #to move num_of_crates, we pop as many times as the number of crates
        # we pop from the array with index from_arr_index
        # we append to the array with index to_arr_index
        temp_list = []
        array_to_pop = arrays[from_arr_index]
        arry_to_append = arrays[to_arr_index]
        for x in range (num_of_crates):     
            temp_list.insert(0,array_to_pop.pop())
        print('temp list {}'.format(temp_list))

        arry_to_append.extend(temp_list)
        print('array to append {}'.format(arry_to_append))
        print('new status of arrays: {}'.format(arrays))
    return arrays

def get_crates_on_top(final_arrays):

    #we need to know how many stacks we have
    num_of_stacks = len(final_arrays)
    final_string = ''

    for index in range(num_of_stacks):
        final_string +=final_arrays[index].pop()
        #print(final_string)

    return final_string

def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path_stacks = dir_path +"/stacks2.csv"
    input_path_instructions = dir_path +"/instructions2.csv"
    #print(input_path)

    stacks = read_csv(input_path_stacks)
    print(stacks)
    instructions = read_csv(input_path_instructions)
    #print(instructions)

    final_arrays = follow_instructions(instructions, stacks)

    combination_of_crates_on_top = get_crates_on_top(final_arrays)

    print(combination_of_crates_on_top)

    #part2 
    stacks2 = read_csv(input_path_stacks)
    final_arrays2 = follow_instructions_p2(instructions, stacks2)

    print(final_arrays2)

    combination_of_crates_on_top_2 = get_crates_on_top(final_arrays2)

    print(combination_of_crates_on_top_2)

    return 0

if __name__ == "__main__":
    main()

