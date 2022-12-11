#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv
import math

def read_csv(path):

    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        data2 = [row[0] for row in data]

    return data2

def calculate_distance_between_points(pointa, pointb):

    return math.dist((pointa,),(pointb,))

def is_diagonally_adjacent(tuple1, tuple2):
    # Check if the tuples have the same length and contain only integers
    if len(tuple1) != len(tuple2) or not all(isinstance(x, int) for x in tuple1 + tuple2):
        return False
    
    # Check if the absolute difference between the elements of the tuples is equal to 1
    for i in range(len(tuple1)):
        if abs(tuple1[i] - tuple2[i]) != 1:
            return False
    
    # If the code reaches this point, the tuples are diagonally adjacent
    return True



def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = dir_path +"/input.csv"
    #print(input_path)

    input = read_csv(input_path)
    print(input)

    #part 1
    x = 0
    y = 0
    tale_points = {}
    starting_postion = (x,y)
    head_position = starting_postion
    tail_position = starting_postion



    # for move in input:
    # #move = input[0]
    #     direction = move.split(' ')[0]
    #     steps = int(move.split(' ')[1])
        
    #     print(move)
    #     for step in range(steps):
    #         print('step {}.'.format(step+1))

    #         if direction == 'U':
    #             #we move up
    #             x+=1
                
    #         elif direction == 'D':
    #             #we move down
    #             x-=1
                
    #         elif direction == 'R':
    #             #we move right
    #             y+=1
                        
    #         elif direction == 'L':
    #             #we move left
    #             y-=1
                
    #         head_position = (x,y)
    #         #once the head completes it's move, we need to check the postion of the tail relative to the head
    #         #check if we are in the same row (head_x == tail_x)
    #         head_x = head_position[0]
    #         head_y = head_position[1]
    #         tail_x = tail_position[0]
    #         tail_y = tail_position[1]
    #         print('Head position after step: {}'.format(head_position))

    #         if head_x == tail_x and (head_y == tail_y):
    #             print('touching, tail stays the same')
    #         elif head_x == tail_x and not (head_y == tail_y):
    #             print('same row')
    #             #we are in the same row, the tail should only move 1step if the head is 2 steps ahead
    #             distance = calculate_distance_between_points(head_y,tail_y)

    #             print('distance between points: {}'.format(distance))
    #             if distance >=2:
    #                 # we need to see if the head is right or left from the tail
    #                 if head_y > tail_y:
    #                     #the head is to the right of tail
    #                     #the tail needs to move one step to the right
    #                     tail_y+=1
    #                 else:
    #                     #the head is to to the left of the tail
    #                     #the tail needs to move one step to the left
    #                     tail_y-=1
    #         elif head_y == tail_y and not (head_x == tail_x):
    #             print('same column')
    #             #we are in the same column, the tail should only move 1step if the head is 2 steps ahead
    #             distance = calculate_distance_between_points(head_x,tail_x)
    #             print('distance between points: {}'.format(distance))
    #             if distance >=2:
    #                 # we need to see if the head is up or down from the tail
    #                 if head_x > tail_x:
    #                     #the head is above the tail
    #                     #the tail needs to move one step to the top
    #                     tail_x+=1
    #                 else:
    #                     #the head is below the tail
    #                     #the tail needs to move one step to the bottom
    #                     tail_x-=1       
    #         else:
    #             distance1 = calculate_distance_between_points(head_x,tail_x)
    #             distance2 = calculate_distance_between_points(head_y,tail_y)
    #             print('distance 1 {} and distance 2 {}'.format(distance1,distance2))
    #             #If the absolute value of the difference between the x values is the same as the absolute value of the difference between the y values,
    #             #  then the tuples are diagonal to each other.
    #             if distance1 != distance2:
    #                 print('diagonal move')
    #                 #we are not in the same row and we are not in the same column, we will need to make a diagonal move
    #                 #we need to understand where head is compared to the tail
    #                 if head_x > tail_x:
    #                     #the head is above the tail
    #                     #the tail needs to move one step to the top
    #                     tail_x+=1
    #                 else:
    #                     #the head is below the tail
    #                     #the tail needs to move one step to the bottom
    #                     tail_x-=1

    #                 if head_y > tail_y:
    #                     #the head is to the right of tail
    #                     #the tail needs to move one step to the right
    #                     tail_y+=1
    #                 else:
    #                     #the head is to to the left of the tail
    #                     #the tail needs to move one step to the left
    #                     tail_y-=1
    #             else:
    #                 print('no move, they connect diagonically')

    #         tail_position = (tail_x,tail_y)

    #         print('Tail position after step: {}'.format(tail_position))
    #         #add tail position to dictionary
    #         #check if the key exists:
    #         if tail_position not in list(tale_points.keys()):
    #             #first time we visit the point, we should add it in the list
    #             print('fist time we visit')
    #             tale_points[tail_position] = 1
    #         else:
    #             #we have visited this point again:
    #             print('tail has visited again')
    #             tale_points[tail_position] += 1

            

    #     print('Steps finished. Head: {}, Tail: {}.'.format(head_position, tail_position))

    #     print('Tale points: {}'.format(tale_points))

    # print('Total unique positions the tail visited: {}'.format(len(list(tale_points.keys()))))


    # part 2

    tuples = [head_position,(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),tail_position]
    

    for move in input:
    #move = input[0]
        direction = move.split(' ')[0]
        steps = int(move.split(' ')[1])
        
        print(move)
        for step in range(steps):
            print('step {}.'.format(step+1))
            for i in range(1,len(tuples)):            
                print('index {}.'.format(i))
                leading_knot = tuples[i-1]

                if i == 1:
                    #it means that our leading knot is the head and we should actually change position
                    x=0
                    y=0

                    if direction == 'U':
                        #we move up
                        x=1
                        
                    elif direction == 'D':
                        #we move down
                        x=-1
                        
                    elif direction == 'R':
                        #we move right
                        y=1
                                
                    elif direction == 'L':
                        #we move left
                        y=-1
                    print('head before {}'.format(leading_knot))
                    #print('X,Y {} {}'.format(x,y))
                    updated_x = leading_knot[0]+x
                    #print(f'updated x {updated_x}')
                    updated_y = leading_knot[1]+y
                    #print(f'updated y {updated_y}')
                    tuples[i-1]  = (updated_x, updated_y)  
                    leading_knot = tuples[i-1]
                    print('head after {}'.format(leading_knot))
                    #once the head completes it's move, we need to check the postion of the tail relative to the head
                    #check if we are in the same row (head_x == tail_x)
                    head_x = leading_knot[0]
                    head_y = leading_knot[1]

                    following_knot = tuples[i]
                    tail_x = following_knot[0]
                    tail_y = following_knot[1]
                    print('Head position after step: {}'.format(leading_knot))

                    if head_x == tail_x and (head_y == tail_y):
                        print('touching, following knot stays the same')
                    elif head_x == tail_x and not (head_y == tail_y):
                        #print('same row')
                        #we are in the same row, the tail should only move 1step if the head is 2 steps ahead
                        distance = calculate_distance_between_points(head_y,tail_y)

                        print('distance between points: {}'.format(distance))
                        if distance >=2:
                            # we need to see if the head is right or left from the tail
                            if head_y > tail_y:
                                #the head is to the right of tail
                                #the tail needs to move one step to the right
                                tail_y+=1
                            else:
                                #the head is to to the left of the tail
                                #the tail needs to move one step to the left
                                tail_y-=1
                    elif head_y == tail_y and not (head_x == tail_x):
                        #print('same column')
                        #we are in the same column, the tail should only move 1step if the head is 2 steps ahead
                        distance = calculate_distance_between_points(head_x,tail_x)
                        print('distance between points: {}'.format(distance))
                        if distance >=2:
                            # we need to see if the head is up or down from the tail
                            if head_x > tail_x:
                                #the head is above the tail
                                #the tail needs to move one step to the top
                                tail_x+=1
                            else:
                                #the head is below the tail
                                #the tail needs to move one step to the bottom
                                tail_x-=1       
                    elif is_diagonally_adjacent(leading_knot,following_knot):
                        print("The tuples are diagonally adjacent")
                        #print('distance 1 {} and distance 2 {}'.format(distance1,distance2))
                        #If the absolute value of the difference between the x values is the same as the absolute value of the difference between the y values,
                        #  then the tuples are diagonal to each other.
                    else:
                        print('diagonal move')
                        #we are not in the same row and we are not in the same column, we will need to make a diagonal move
                        #we need to understand where head is compared to the tail
                        if head_x > tail_x:
                            #the head is above the tail
                            #the tail needs to move one step to the top
                            tail_x+=1
                        else:
                            #the head is below the tail
                            #the tail needs to move one step to the bottom
                            tail_x-=1

                        if head_y > tail_y:
                            #the head is to the right of tail
                            #the tail needs to move one step to the right
                            tail_y+=1
                        else:
                            #the head is to to the left of the tail
                            #the tail needs to move one step to the left
                            tail_y-=1

                    tuples[i] = (tail_x,tail_y)
                    following_knot = tuples[i]

                    print('Following knot position after step: {}'.format(following_knot))
                    #add tail position to dictionary
                    #check if the key exists:
                else:
                    #for every other case, once we moved the head we have to compare the position of the other elements between them
                    leading_knot = tuples[i-1]
                    #once the head completes it's move, we need to check the postion of the tail relative to the head
                    #check if we are in the same row (head_x == tail_x)
                    head_x = leading_knot[0]
                    head_y = leading_knot[1]

                    following_knot = tuples[i]
                    tail_x = following_knot[0]
                    tail_y = following_knot[1]
                    print('Leading Knot position after step: {}'.format(leading_knot))

                    if head_x == tail_x and (head_y == tail_y):
                        print('touching, following knot stays the same')
                    elif head_x == tail_x and not (head_y == tail_y):
                        #print('same row')
                        #we are in the same row, the tail should only move 1step if the head is 2 steps ahead
                        distance = calculate_distance_between_points(head_y,tail_y)

                        print('distance between points: {}'.format(distance))
                        if distance >=2:
                            # we need to see if the head is right or left from the tail
                            if head_y > tail_y:
                                #the head is to the right of tail
                                #the tail needs to move one step to the right
                                tail_y+=1
                            else:
                                #the head is to to the left of the tail
                                #the tail needs to move one step to the left
                                tail_y-=1
                    elif head_y == tail_y and not (head_x == tail_x):
                        #print('same column')
                        #we are in the same column, the tail should only move 1step if the head is 2 steps ahead
                        distance = calculate_distance_between_points(head_x,tail_x)
                        print('distance between points: {}'.format(distance))
                        if distance >=2:
                            # we need to see if the head is up or down from the tail
                            if head_x > tail_x:
                                #the head is above the tail
                                #the tail needs to move one step to the top
                                tail_x+=1
                            else:
                                #the head is below the tail
                                #the tail needs to move one step to the bottom
                                tail_x-=1       
                    elif is_diagonally_adjacent(leading_knot,following_knot):
                        print("The tuples are diagonally adjacent")
                        #print('distance 1 {} and distance 2 {}'.format(distance1,distance2))
                        #If the absolute value of the difference between the x values is the same as the absolute value of the difference between the y values,
                        #  then the tuples are diagonal to each other.
                    else:
                        print('diagonal move')
                        #we are not in the same row and we are not in the same column, we will need to make a diagonal move
                        #we need to understand where head is compared to the tail
                        if head_x > tail_x:
                            #the head is above the tail
                            #the tail needs to move one step to the top
                            tail_x+=1
                        else:
                            #the head is below the tail
                            #the tail needs to move one step to the bottom
                            tail_x-=1

                        if head_y > tail_y:
                            #the head is to the right of tail
                            #the tail needs to move one step to the right
                            tail_y+=1
                        else:
                            #the head is to to the left of the tail
                            #the tail needs to move one step to the left
                            tail_y-=1
                    tuples[i] = (tail_x,tail_y)
                    following_knot = tuples[i]

                    print('Following knot position after step: {}'.format(following_knot))

                    
                #when we are in the last knot (i ==9), we want to add the new point if the tail moves
                if i == 9:
                    print('we are in the actual tail')                    
                    if following_knot not in list(tale_points.keys()):
                        #first time we visit the point, we should add it in the list
                        print('fist time we visit')
                        tale_points[following_knot] = 1
                    else:
                        #we have visited this point again:
                        print('tail has visited again')
                        tale_points[following_knot] += 1

                

        print('Steps finished. knot positions: {}'.format(tuples))

        print('Tale points: {}'.format(tale_points))

    print('Total unique positions the tail visited: {}'.format(len(list(tale_points.keys()))))


    return 0


if __name__ == "__main__":
    main()