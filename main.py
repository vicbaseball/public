from string import punctuation, whitespace
import sys

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
            if letter not in punctuation and letter!=whitespace and letter not in "0987654321":
                if letter!=" ":
                    letter = letter.lower()
                line+=letter
            else:
                line+=" "
        words+=[line]
        file_line = file.readline()
    file.close()
    outputfile.writelines(words)
    return words

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

def words_in_bk(path_to_book):
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
    return Dictionary

def words_in_book_not_list(path_to_book):
    words_in_book = words_in_bk(path_to_book)
    words_in_wrdtxt = words_in_bk("words.txt")

    words_not_in_book = []
    # word1 is word in book
    # word2 is words in the words.txt
    for word1 in words_in_book:
        for word2 in words_in_wrdtxt:
            if set(word1)-set(word2)!=set() or len(word1)!=len(word2):
                words_not_in_book.append(word1)
                break
    return words_not_in_book





#print(count_word("test.txt"))
#print(words_extraction("test.txt"))

print(words_in_book_not_list("test.txt"))
