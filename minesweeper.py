# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:16:13 2022
Student:shani dighorker

Assignmet no:3
Program:minesweeper.py
"""

import random
import copy  # donita approve to use copy
from typing import List

play_bord = int(input("Please enter a number of NxN (max 9):  "))
mines = int(input("Please enter number of mines: "))
while play_bord > 9:  # check no more then 9 for NxN
    print("You have selected more then 9")
    play_bord = int(input("Please enter a number of row (max 9):  "))

while mines > 2 * play_bord:  # check it's no more then 2n
    print("too many mines do again")
    mines = int(input("Please enter number of mines: "))


def create_random_list(n, bombs):
    "First of all we cread list inside of list for the "
    grip = [[" " for i in range(0, n + 2)] for j in range(0, n + 2)]  # i make here +2 because to create
    # more 1 column and row for system not send msg out of range
    rndi = random.randint(1, n - 2)
    rndj = random.randint(1, n - 2)
    for i in range(2, bombs + 2):  # enter the mines randomaly to the list
        while grip[rndi][rndj] == "*":
            rndi = random.randint(1, n)
            rndj = random.randint(1, n)
        grip[rndi][rndj] = "*"
    return grip


def print_bord(arr):
    " here aot of print that make the print go well"
    arr = arr[1:-1]
    print("   ", 1, end="   ")
    for j in range(1, len(arr)):
        print(j + 1, end="   ")
    print()
    for i in range(0, len(arr)):
        print("  ", end="")
        print("+---" * len(arr), end="+")
        print()
        print(i + 1, end=" ")
        for j in range(1, len(arr) + 1):
            print("|", end="")
            if not j == len(arr) + 1:
                print(" {0} ".format(arr[i][j]), end="")
        print("", end="|")
        print()
    print("  ", end="")
    print("+---" * len(arr), end="+")
    print()


def update_number_of_bomb_around(arr, x, y):
    "this funcion is to check bombs around and update the print"
    if x < 1 or x > len(arr) - 2 or y < 1 or y > len(arr) - 2:  # make sure it's not out of range
        return
    sum1 = 0
    if arr[x][y] == "*":  # if the spot is mines stop the function
        return
    for k in range(-1, 2):
        for l in range(-1, 2):
            if arr[x + k][y + l] == "*":  # this to check mines around and update
                sum1 += 1
    arr[x][y] = sum1  # update how many mines around
    if arr[x][y] == 0:
        arr[x][y] = "+"  # just check it from 0 to +


def open_map(arr):
    "this function is to open all map(Answer)"
    for i in range(1, (len(arr) - 1)):
        for j in range(1, (len(arr) - 1)):
            update_number_of_bomb_around(arr, i, j)


def close_map(arr):
    "and this to close to map"
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i][j] != "*":
                arr[i][j] = " "


def check_if_lost(arr, x, y):
    "function that check if u hit a mine"
    if arr2[x][y] == "*":
        return True
    else:
        return False


def hide_spot(arr):
    "for the arr to close all and make it ' ' "
    for i in range(1, (len(arr) - 1)):
        for j in range(1, (len(arr) - 1)):
            arr[i][j] = " "


def check_if_win(arr):
    "function to check if the player win"
    lst = [1, 2, 3, 4, 5, 6, 7, 8, "-"]
    sum_for_check = 0
    for i in range(1, (len(arr) - 1)):
        for j in range(1, (len(arr) - 1)):
            if arr[i][j] in lst:  # check if not a bomb and not spot open yet
                sum_for_check += 1  # add 1 if not
    if sum_for_check == ((play_bord ** 2) - mines):  # here to check if win, if everything open it's
        # sholde be equal to amount spot on game bord - the mines
        return True
    else:
        return False


arr = create_random_list(play_bord, mines)
open_map(arr)
arr2 = copy.deepcopy(arr)
close_map(arr)
hide_spot(arr)


def rec(arr, x, y):
    " and here is the recursion that open all what is '0' or as i change it to be '+'"
    movement = [(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1), (0, 1), (0, -1)]
    if x < 1 or x > len(arr) - 2 or y < 1 or y > len(arr) - 2:  # Stop conditions out of range
        return
    if arr2[x][y] == "*":  # Stop conditions if u on mine
        return
    if arr[x][y] == "-":  # Stop conditions if u alerdy check that spot
        return
    update_spot(arr, x, y)
    if arr2[x][y] == "+":  # start run on all open spot no mines around
        arr[x][y] = "-"
        for i, j in movement:
            rec(arr, x + i, y + j)


def update_spot(arr, x, y):
    "update the game bord of the player to the 'Answer' "
    arr[x][y] = arr2[x][y]


while True:
    "and here all magic happen for the player"

    print_bord(arr)
    print()
    x = int(input("Enter a row: "))
    y = int(input("Enter a column:  "))
    update_spot(arr, x, y)
    if arr[x][y] == "+":
        rec(arr, x, y)
    if check_if_lost(arr, x, y):
        print_bord(arr2)
        print("U hit a mine GAME OVER!")
        break
    if check_if_win(arr):
        print("U WON ,great jobe")
        print_bord(arr2)
        break
