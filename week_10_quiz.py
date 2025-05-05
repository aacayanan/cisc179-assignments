def word_stats(file_name):
    # open the file
    infile = open(file_name, 'r')

    # read the file
    file_contents = infile.read()

    # close the file
    infile.close()

    # get the number of words, separated by whitespace
    words = file_contents.split()
    num_words = len(words)

    # get the average length of the words
    total_length = 0
    avg_length = 0
    for word in words:
        total_length += len(word)
        avg_length = total_length / num_words

    print(f"Total words: {num_words}")
    print(f"Average length: {avg_length}")
