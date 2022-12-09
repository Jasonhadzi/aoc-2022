#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import csv

def read_csv(path):

    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile,delimiter=','))
        # we split the string ['1234'] to ['1','2','3','4']
        data1 = [list(row[0]) for row in data]
        # we make each character in the row from string to int
        data2 = [list(map(int, row)) for row in data1]

    return data2

# Function to calculate the scenic score of a tree
def scenic_score(array, i, j,row,col):
    i_orig = i
    j_orig = j
    print('row_col:({},{}), value: {}'.format(i_orig,j_orig,array[i,j]))
    #print(array[i,j])
    # Check the view in each direction and count the number of trees seen
    up = 0
    while i > 0 and array[i-1,j] <= array[i_orig,j_orig]:
        up += 1
        i -= 1
    
    i = i_orig
    down = 0
    #i = i_orig + up + 1
    while i < row - 1 and array[i+1,j] <= array[i_orig,j_orig]:
        down += 1
        i += 1
    
    i = i_orig
    j = j_orig
    
    left = 0
    while j > 0 and array[i,j-1] <= array[i_orig,j_orig]:
        left += 1
        j -= 1
    
    j = j_orig
    right = 0
    #j = j_orig + left + 1
    while j < col - 1 and array[i,j+1] <= array[i_orig,j_orig]:
        right += 1
        j += 1
   
    print('up,down,left,right {} {} {} {}'.format(up , down , left , right))
    print('max score {}'.format(up * down * left * right ))
    return up * down * left * right 


def total_visible_trees(array,row, col):

    visible_trees = 0
    for row_index in range(row):
        for col_index in range(col):
            item_to_explore = array[row_index,col_index]
            # tree is visible if all of the other trees between it 
            # and an edge of the grid are shorter than it.
            # Only consider trees in the same row or column; that is, 
            # only look up, down, left, or right from any given tree.

            # All of the trees around the edge of the grid are visible
            if (row_index == 0 or row_index == row-1) or (col_index == 0 or col_index == col-1):
                
                print('row_col:({},{}), value: {}'.format(row_index,col_index,item_to_explore))
                print('we are on the edge, tree is visible')
                visible_trees +=1
            else:
                print('row_col:({},{}), value: {}'.format(row_index,col_index,item_to_explore))
                print('interior tree')
                visible_from = []
                #we need to look up, down, left, or right from any given tree.
                #look left
                left_tree = array[row_index,:col_index].max()
                
                #look right
                right_tree = array[row_index,col_index+1:].max()
                #look up
                up_tree = array[:row_index,col_index].max()
                #print(up_tree)
                #look down
                down_tree = array[row_index+1:,col_index].max()

                if item_to_explore > left_tree:                    
                    visible_from.append('left')
                elif item_to_explore > right_tree:                    
                    visible_from.append('right')
                elif item_to_explore > up_tree:
                    #print('got here')
                    visible_from.append('top')
                elif item_to_explore > down_tree: 
                    visible_from.append('down')
                else:
                    print('tree is not visible')
                
                #print('row_col:({},{}), value: {}'.format(row_index,col_index,item_to_explore))
                if len(visible_from):
                    print('tree is {}'.format(visible_from))
                    visible_trees +=1

    return visible_trees



def main():
    """ Main program """
    # Code goes over here.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = dir_path +"/input2.csv"
    #print(input_path)

    input = read_csv(input_path)

    
    print(input)
    print('Number of rows in input:', len(input))

    A = np.array(input)
    #shape is (number of rows, number of columns)
    print(A.shape)

    row, col = A.shape
    print(row)
    print(col)
    # size (= total number of elements)
    print(A.size)
    
    # print(A)
    # print(A[:3,0])
    # print(A[1,:2])
    # print(A[1,:])
    # print(A[1,:].max())
    # print(A[2,1])

    # part 1

    visible_trees = total_visible_trees(A,row,col)
                
    print('total visible trees: {}'.format(visible_trees))
    print('total invisible trees: {}'.format(A.size - visible_trees))

    #part 2
    print('part 2')
    # # Calculate the scenic score of each tree and find the maximum
    # max_score = 0
    # for row_index in range(row):
    #     for col_index in range(col):
    
    
    #         max_score = max(max_score, scenic_score2(input,row_index,col_index))

    # # Print the maximum scenic score
    # print(max_score)

    itxt = open("input2.csv", mode='r').read().splitlines()
    tree = {(x,y): t for y, row in enumerate(itxt) for x, t in enumerate(list(row))}
    visi = {(x,y): 0 for y, row in enumerate(itxt) for x, _ in enumerate(list(row))}

    print(tree)
    print(visi)
    for xt, yt in tree.keys():
        if xt == 0 or yt == 0 or xt == len(list(itxt)) or yt == len(itxt):
            continue
        
        lr = rl = tb = bt = 0
        
        for xc in range(xt + 1, len(list(itxt))): #l->r
            lr += 1
            
            if tree.get((xc,yt)) >= tree.get((xt,yt)):
                break

        for xc in range(xt - 1, -1, -1): #r->l
            rl += 1
            
            if tree.get((xc,yt)) >= tree.get((xt,yt)):
                break

        for yc in range(yt + 1, len(itxt)): #t->b
            tb += 1
            
            if tree.get((xt,yc)) >= tree.get((xt,yt)):
                break
            
        for yc in range(yt - 1, -1, -1): #b->t
            bt += 1
            
            if tree.get((xt,yc)) >= tree.get((xt,yt)):
                break

        visi.update({ (xt,yt): lr * rl * tb * bt })

    print(sorted(visi.values())[-1])

    return 0

if __name__ == "__main__":
    main()