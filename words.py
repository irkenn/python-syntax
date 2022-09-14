def print_upper_words(words, must_start_with):
    """This function will return each letter of the word in uppercase.
    The letters will be printed in a separate line.
        Arguments:
            words -- will receive a list of words to be converted.
            must_start_with argument -- will receive an object and print the words that start
                                       with the letter listed there.
    """
    output = []
    for first in must_start_with:
        for w in words:
            if first == w[0]:
                output.append(w.upper())
    print(output)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})