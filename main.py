from string import punctuation, whitespace
import itertools

# task 1
def words_extraction(path_to_file):
    # open file
    words = []
    file = open(path_to_file, 'r+')
    outputfile = open("output_file.txt", "w")

    # first line in txt
    file_line = file.readline()
    while file_line:
        # intialize modified line
        line = ""
        # loop through file and check for punctations and whitespaces
        for letter in file_line:
            if letter not in punctuation and letter!=whitespace:
                if letter!=" ":
                    letter = letter.lower()
                line+=letter
        words+=[line]
        file_line = file.readline()
    file.close()
    outputfile.writelines(words)
    return words

words_extraction("test.txt")

def count_word(path_to_book):
    # words is a list of strings, where each string is the lines of the book from perevious function
    book = words_extraction(path_to_book)
    Dictionary = dict()

    # loop trhough lines in words variable for preface line to mark beginning of book
    for i in range(len(book)):
        # we found line
        if "start of the project" in book[i]:
            # ignore every previous line
            book = book[i+1:]
            break

    for line in book:
        # words is a list of each word in line
        words = line.split(" ")
        for word in words:
            # remove whitespaces and new line symbols
            word = word.replace("\n", "")
            if word=="":
                continue
            # intialize count for word
            if word not in Dictionary:
                Dictionary[word]=0
            # increment word frequency
            Dictionary[word]+=1
    return len(Dictionary)

print(count_word("test.txt"))
