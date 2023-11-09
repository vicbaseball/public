from string import punctuation, whitespace

def words_extraction(path_to_file):
    # open file
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
        outputfile.writelines([line, "\n"])
        file_line = file.readline()
    file.close()


words_extraction('test.txt')
