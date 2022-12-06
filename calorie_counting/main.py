#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os
import csv

def read_input(path, header=None):

    input = pd.read_csv(path, header=header)

    return input


def read_csv(path):
    

    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    return data


def create_dict_from_list(list):

    elves_dict = {}
    
    #if the array item is empty it means a new elf is starting
    elf_index =0
    for calorie in list:
        if len(calorie)==1:
            print(calorie[0])
            if elf_index not in elves_dict:
                elves_dict[elf_index] = []
            elves_dict[elf_index].append(int(calorie[0]))
        else:
            print('empty row, we completed the {} elf.'.format(elf_index))
            elf_index +=1
    
    return elves_dict

def get_max_per_elf(elves_dict):
    elves_sum = {}

    for index, calories in elves_dict.items():

        #print(index, sum(calories))
        elves_sum[index] = sum(calories)

    return elves_sum

        
        



def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = dir_path +"/input.csv"
    #print(input_path)

    calories_list = read_csv(input_path)

    elves_dict = create_dict_from_list(calories_list)

    #print(elves_dict)

    elves_max = get_max_per_elf(elves_dict)
    #print(elves_max)
    
    #get elf with max calories
    key_with_max_value = max(elves_max, key=elves_max.get)
    print(key_with_max_value)
    max_value = elves_max[key_with_max_value]
    print(max_value)

    #get max value
    all_values = elves_max.values()
    max_value_2nd_way = max(all_values)
    print(max_value_2nd_way)

    sorted_dict = dict(sorted(elves_max.items(), key=lambda item: item[1]))
    print(sorted_dict)
    
    return 0

if __name__ == "__main__":
    main()