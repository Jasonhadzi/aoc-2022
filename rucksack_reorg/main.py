#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv
import string





def generate_prio_dict():
    low_prio = dict(zip(string.ascii_lowercase, range(1,27)))
    high_prio = dict(zip(string.ascii_uppercase, range(27,53)))
    
    final_dict = {**low_prio, **high_prio}

    return final_dict


def find_common_element(s_1, s_2):
    common_elements = list(set(s_1) & set(s_2))
    
    return common_elements

def find_common_element_p2(group_of_items):
    s_1 = group_of_items[0]
    s_2 = group_of_items[1]
    s_3 = group_of_items[2]
    common_elements = list(set(s_1) & set(s_2)& set(s_3))
    
    return common_elements

def number_of_groups_to_split(data):

    #get number of rows:
    num_of_rows = len(data)

    #we have 3 elves so we will make a group of 3
    num_of_groups_to_create = num_of_rows / 3

    return int(num_of_groups_to_create)

def divide_string_in_half(string_line):

    len_of_string = len(string_line)
    print('len is {}'.format(len_of_string))

    index_to_split = int(len_of_string/2)
    print('index to split {}'.format(index_to_split))

    print('initial string: {}'.format(string_line))
    string_one = string_line[0:index_to_split]
    string_two = string_line[index_to_split:]

    print('string 1: {}'.format(string_one))
    print('string 2: {}'.format(string_two))

    return string_one, string_two


def read_csv(path):
    

    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        data2 = [row[0] for row in data]

    return data2



def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = dir_path +"/input.csv"
    #print(input_path)

    input_csv = read_csv(input_path)
    print(input_csv)

    priorities_dict = generate_prio_dict()

    #print(priorities_dict)

    #part 1
    # rucksack_dict = {}
    # rucksack_index =0
    # for rucksack in input_csv:
    #     if len(rucksack)>0:
    #         s_1, s_2 = divide_string_in_half(rucksack)
            
    #         rucksack_dict[rucksack_index] = find_common_element(s_1,s_2)
    #         common_element = rucksack_dict[rucksack_index][0]
    #         print('common element: {}'.format(common_element))

            
    #         #find value of common element
    #         value = priorities_dict[common_element]
    #         print('common element priority: {}'.format(value))

    #         #prioriry of common element per racksack
    #         rucksack_dict[rucksack_index] = value

    #         rucksack_index +=1

    # print(rucksack_dict)

    # sum_of_prio_of_common_values = sum(rucksack_dict.values())
    # print(sum_of_prio_of_common_values)
    

    #part 2
    #the number of items of the input array is the number of rows of the input
    #we divide the number of rows by 3 to get the number of groups we should split
    step = number_of_groups_to_split(input_csv)
    np_array = np.array(input_csv)
    arrays = np.split(np_array, step)

    rucksack_dict = {}
    rucksack_index =0

    for group in arrays:
        print('group: {}'.format(group))
        common_element = find_common_element_p2(group)[0]
        print('common element: {}'.format(common_element))

            
        #find value of common element
        value = priorities_dict[common_element]
        print('common element priority: {}'.format(value))
        rucksack_dict[rucksack_index] = value
        rucksack_index +=1
    print(rucksack_dict)

    sum_of_prio_of_common_values = sum(rucksack_dict.values())
    print(sum_of_prio_of_common_values)

    return 0

if __name__ == "__main__":
    main()