"""
    expand_chunk

    Paramater
    > Takes in 512-bit binary string

    Algorithm
    > Breaks up input into sixteen 32-bit words
    > Creates 64 new 32-bit words based off the original 16
    > Appends the new words to the original list of 16

    Return Value
    > Returns a list of 80 32-bit words in the form of bianry strings
    
"""

def expand_chunk(string_512bits):

    # Break up chunks into sixteen 32-bit words
    word_list = []
    for i in range(0, 512, 32):
        word_list.append(string_512bits[i:i+32])


    # Iterate through word_list, starting at 16 and ending at 79.
    # Select the words that are at i-3, i-8, i-14, and i-16 for each iteration.
    for i in range(16, 80, 1):
        word1 = int(word_list[i-3], 2)
        word2 = int(word_list[i-8], 2)
        word3 = int(word_list[i-14], 2)
        word4 = int(word_list[i-16], 2)

        # XOR all the selected words
        new_word = bin(word1 ^ word2 ^ word3 ^ word4)[2:].zfill(32)

        # Rotate the new word left 1
        temp = new_word[0]
        new_word = new_word[1:]
        new_word += temp

        # Append new word to original word_list
        word_list.append(new_word)

    return word_list
