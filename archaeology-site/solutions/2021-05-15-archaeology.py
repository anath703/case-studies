#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:44:36 2021

@author: connorkillion
"""
import pandas as pd
import seaborn as sns
df = pd.read_csv("nails.csv")
x = -1
        # A B C D E F G H I J
grid = [[x,x,x,x,x,x,x,x,x,x], #1
        [x,x,x,x,x,x,x,x,x,x], #2
        [x,x,x,x,x,x,x,x,x,x], #3
        [x,x,100,x,x,x,x,x,x,x], #4
        [x,x,x,x,x,1,0,x,x,x], #5
        [x,75,x,x,x,x,x,1,x,0], #6
        [x,x,x,33,x,x,x,x,x,0], #7
        [45,77,x,x,x,x,x,3,x,x], #8
        [x,x,x,x,x,x,x,x,x,x], #9
        [x,x,x,x,x,x,x,x,x,x]] #10


final_weight = 0
total_distance = 0

dictionary = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6,
              "H":7, "I":8, "J":9}

def num_nails(letter, number):
    try:
        y = int(letter)
    except ValueError:
        y = dictionary[letter]
    final_weight = 0
    total_distance = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] != -1:
                distance = ((((i - number)**2)+((j-y)**2))**0.5)
                total_distance += (1/distance)
                weight = (1/distance) * grid[i][j]
                final_weight += weight
    final = round(final_weight / total_distance)
    #print("Number of nails:", final)
    return final
    
heatmap = []
for i in range(10):
    x = []
    for j in range(10):
        if grid[i][j] == -1:
           res = num_nails(j,i)
           x.append(res)
        else:
            x.append(grid[i][j])
    heatmap.append(x)

sns.heatmap(heatmap)
print("Number of nails: ", num_nails("D", 4))           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
