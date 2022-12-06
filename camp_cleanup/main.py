#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv
import string


def expand_strings(group1,group2):
    #print('group1 {}, group2 {}'.format(group1,group2))
  
    group1_start = int(group1.split('-')[0])
    group1_end = int(group1.split('-')[1])+1

    group2_start = int(group2.split('-')[0])
    group2_end = int(group2.split('-')[1])+1

    p1 = list(range(group1_start,group1_end))
    p2 = list(range(group2_start,group2_end))

    #print('pair1 {}, pair2 {}'.format(p1,p2))
    return [p1,p2]

def expanded_array(input_csv):

    expanded_array = []
    for pairs in input_csv:
        
        expanded_array.append(expand_strings(pairs[0],pairs[1]))

    return expanded_array

def pairs_completely_overlap(array):

    total_num_of_overlaps = 0
    for pairs in array:
        pair1 = pairs[0]
        pair2 = pairs[1]

        flag = 0
        if(set(pair1).issubset(set(pair2))) or (set(pair2).issubset(set(pair1))):
            flag = 1
            total_num_of_overlaps +=1
        if (flag):
            print("Yes, list is subset of other.")
        else:
            print("No, list is not subset of other.")
    return total_num_of_overlaps

def pairs_partialy_overlap(array):

    num_of_overlaps = 0

    for pairs in array:
        pair1 = pairs[0]
        pair2 = pairs[1]
        flag =0
        if (list(set(pair1) & set(pair2))):
            flag =1
            num_of_overlaps +=1
        if (flag):
            print("Yes, they overlap.")
        else:
            print("No, they don't overlap.")
    
    return num_of_overlaps


def read_csv(path):

    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile,delimiter=','))
    return data

def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = dir_path +"/input.csv"
    #print(input_path)

    input_csv = read_csv(input_path)
    print(input_csv)

    
    new_array = expanded_array(input_csv)

    print(new_array)

    overlaps = pairs_completely_overlap(new_array)

    print(overlaps)     

    partial_overlaps = pairs_partialy_overlap(new_array)

    print(partial_overlaps)

    return 0

if __name__ == "__main__":
    main()
