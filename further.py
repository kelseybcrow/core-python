from fileinput import filename
import random
import os
import sys

# get txt files from current directory


def get_files():
    documents = []

    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename[-3:] == 'txt':
            documents.append(filename)

    return documents

# allow user to select a file


def select_file(data):
    for index, filename in enumerate(data):
        print(index + 1, filename)

    data_number = int(input('Select a file # or press enter to exit'))

    return data[data_number-1]

# read scores file and return dictionary of {restaurant-name: score}


def process_scores(filename):
    scores_txt = open(filename)
    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(':')
        scores[restaurant] = int(score)

    return scores

# give user a choice of actions and return the user's choice


def get_action_choice():
    print()
