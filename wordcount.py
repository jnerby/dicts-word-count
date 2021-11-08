"""Count words in file."""
def count_words(filename):

    file = open(filename)

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

# call function
count_words("twain.txt")
