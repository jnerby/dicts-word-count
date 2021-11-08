"""Count words in file."""
import sys

def count_words():

    file = open(sys.argv[1])

    # initialize empty dict
    result = {}

    # split text file by spaces
    for line in file:
        # get list words from text file
        line = line.strip().split(" ")
        # iterate through strings in list of words
        for word in line:
        # if word exists, add 1. if word doesn't exist, create key w/ value 1
            result[word] = result.get(word, 0) + 1

    file.close()

    for word, value in result.items():
        print(word, value)

def tokenize():
    file = open(sys.argv[1])

    # initialize empty tokens list
    tokens = []

    # split text file by spaces
    for line in file:
        # get list words from text file
        line = line.strip().split(" ")
        # loop through words
        for word in line:
            # if word is not tokens list
            if word not in tokens:
                # add to tokens
                tokens.append(word)
    
    file.close()

    return tokens

# call function
print(tokenize())
