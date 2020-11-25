#!/usr/bin/env python3
import argparse
import random


'''Setup'''

# Functions


def random_choice(dict):
    keys = list(dict.keys())
    choice = random.choice(keys)
    return (choice, dict[choice])


# Parser
parser = argparse.ArgumentParser()
parser.add_argument('file_path', help="The file to open with the definitions")
parser.add_argument(
    '-r', '--reverse', help="Reverse keys and definitions", action="store_true")
parser.add_argument('-l', '--length', default=0, type=int,
                    help='Length of the test (all of the definitions if not set)')
args = parser.parse_args()

# Definitions
definitions = dict()

with open(args.file_path, "r") as file:
    for line in file:
        if line[0] != '#':
            if args.reverse:
                key = line.split(":")[1]
                val = line.split(":")[0]
            else:
                key = line.split(":")[0]
                val = line.split(":")[1]
            val = val.replace("\n", "")
            definitions[key] = val


'''Program'''

won = list()
lost = list()

if args.length == 0:
    count = len(definitions)
else:
    count = args.length

# Test
while count > 0:
    choice = random_choice(definitions)
    user = input('What is \033[1m“{}“\033[0m?\n  > '.format(choice[1]))
    definitions.pop(choice[0], None)
    if user == choice[0]:
        won.append(choice)
    else:
        lost.append(choice)
    count -= 1

# Results
print('===')

print('\033[1mYou lost:\033[0m')
for i in lost:
    print('+ \033[1m{}\033[0m which meant \033[1m{}\033[0m'.format(i[1], i[0]))

print('\033[1mYou won: \033[0m')
for i in won:
    print('+ \033[1m{}\033[0m which meant \033[1m{}\033[0m'.format(i[1], i[0]))
