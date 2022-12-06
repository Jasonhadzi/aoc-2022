#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv

def read_csv(path):

    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile,delimiter=','))
        data2 = [row[0] for row in data]
    return data2

def find_start_of_packet(string,num_of_characters):
    starting_four_digits = string[:num_of_characters]
    print(starting_four_digits)
    rest_of_digits = string[num_of_characters:]
    print(rest_of_digits)
    len_of_rest_digits = len(rest_of_digits)

    for index in range(len_of_rest_digits):
        
        print(starting_four_digits)

        if len(set(starting_four_digits)) == len(starting_four_digits):
            print('there are no repeating characters')
            marker = num_of_characters +index
            print('first marker is after character {}'.format(marker))
            break
        else:
            print('there are repeating characters')
            print('we move one index')
            starting_four_digits = starting_four_digits[1:]+rest_of_digits[index]





def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = dir_path +"/input.csv"
    #print(input_path)

    input = read_csv(input_path)
    print(input)

    #part 1
    # for string in input:
    #     find_start_of_packet(string,4)

    #part 2
    for string in input:
        find_start_of_packet(string,14)

    return 0

if __name__ == "__main__":
    main()

