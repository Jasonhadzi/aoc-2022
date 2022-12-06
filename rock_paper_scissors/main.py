#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os

#points (1 for Rock, 2 for Paper, and 3 for Scissors)
#points (0 if you lost, 3 if the round was a draw, and 6 if you won)

#1st column opponent, 2nd column me
#A, X for Rock, 1 point
#B, Y for Paper, 2 points
#C, Z Scissors, 3 points


def read_input(path, header=None, delim_whitespace= True):

    input = pd.read_csv(path, header=header, delim_whitespace=delim_whitespace)

    return input


def strategy_guide(row,points_dict):
    total_points = 0
    opponent_value = row['opponent']
    print('opponent value {}'.format(opponent_value))
    my_value = row['me']
    print('my value {}'.format(my_value))

    my_value_points = points_dict[my_value]
    opponent_value_points = points_dict[opponent_value]
    
    #to cover draw
    if my_value_points == opponent_value_points:
        print("it's a draw, 3 points")
        result = 'Draw'
        total_points += 3
    elif my_value == 'X':
        print('I have Rock')
        if opponent_value == 'B':
            print('opponent has Paper, i lose, 0 points')
            total_points += 0
            result = 'Lose'
        elif opponent_value == 'C':
            print('opponent has Scissors, i win, 6 points')
            total_points += 6
            result = 'Win'
    elif my_value == 'Y':
        print('I have Paper')
        if opponent_value == 'A':
            print('opponent has Rock, i win, 6 points')
            total_points += 6
            result = 'Win'
        elif opponent_value == 'C':
            print('opponent has Scissors, i lose, 0 points')
            total_points += 0
            result = 'Lose'
    elif my_value == 'Z':
        print('I have Scissors')
        if opponent_value == 'A':
            print('opponent has Rock, i lose, 0 points')
            total_points += 0
            result = 'Lose'
        elif opponent_value == 'B':
            print('opponent has Paper, i win, 6 points')
            total_points += 6
            result = 'Win'

    
    extra_points = points_dict[my_value]
    print(extra_points)
    print('extra points {}'.format(extra_points))
    total_points += extra_points
    print('total points {}'.format(total_points))
    final_points = total_points

    
    # result = result
    return final_points


def strategy_guide2(row,points_dict):
    total_points = 0
    opponent_value = row['opponent']
    print('opponent value {}'.format(opponent_value))
    my_result = row['me']
    print('my result {}'.format(my_result))

   
    
    if my_result == 'X':
        print('I need to lose')
        total_points += 0
        if opponent_value == 'A':
            print('Opponent has Rock, I need Scissors')
            my_value = 'Z'
        elif opponent_value == 'B':
            print('Opponent has Paper, I need Rock')
            my_value = 'X'
        elif opponent_value == 'C':
            print('Opponent has Scissors, I need paper')
            my_value = 'Y'
    elif my_result == 'Y':
        print('I need a draw')
        total_points +=3
        if opponent_value == 'A':
            print('Opponent has Rock, I need Rock')
            my_value = 'X'
        elif opponent_value == 'B':
            print('Opponent has Paper, I need Paper')
            my_value = 'Y'
        elif opponent_value == 'C':
            print('Opponent has Scissors, I need Scissors')
            my_value = 'Z'
    elif my_result == 'Z':
        print('I need to win')
        total_points += 6
        if opponent_value == 'A':
            print('Opponent has Rock, I need Paper')
            my_value = 'Y'
        elif opponent_value == 'B':
            print('Opponent has Paper, I need Scissors')
            my_value = 'Z'
        elif opponent_value == 'C':
            print('Opponent has Scissors, I need Rock')
            my_value = 'X'


    
    extra_points = points_dict[my_value]
    print(extra_points)
    print('extra points {}'.format(extra_points))
    total_points += extra_points
    print('total points {}'.format(total_points))
    final_points = total_points

    
    # result = result
    return final_points


def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = dir_path +"/input.csv"
    #print(input_path)

    input_df = read_input(input_path,0)
    print(input_df)
    print(input_df.columns)

    points ={
        'A':1,
        'B':2,
        'C':3,
        'X':1,
        'Y':2,
        'Z':3
    }



    input_df['points'] = input_df.apply(lambda row: strategy_guide(row,points), axis=1)

    #print(input_df)
    print('part 1')
    print(input_df['points'].sum())


    #part2
    #X you need to loose
    #Y you need draw
    #Z you need to win
    print('part 2')
    input_df['points2'] = input_df.apply(lambda row: strategy_guide2(row,points), axis=1)
    print(input_df['points2'].sum())

    return 0

if __name__ == "__main__":
    main()