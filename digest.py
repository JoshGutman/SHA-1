h0 = "01100111010001010010001100000001"
h1 = "11101111110011011010101110001001"
h2 = "10011000101110101101110011111110"
h3 = "00010000001100100101010001110110"
h4 = "11000011110100101110000111110000"

a = h0
b = h1
c = h2
d = h3
e = h4

def digest(word_list):

    # Raise exception if input word_list does not have correct amount of words
    if len(word_list) != 80:
        raise ValueError("Inputted list of words must have 80 words, but instead has {} words".format(str(len(word_list))))

    global a
    global b
    global c
    global d
    global e
    
    
    # Determine which function to use depending on the posisition of the word in word_list
    for i in range(len(word_list)):

        if i <= 19:
            fk = _f1(word_list[i])

        elif i <= 39:
            fk = _f2(word_list[i])

        elif i <= 59:
            fk = _f3(word_list[i])

        else:
            fk = _f4(word_list[i])

        # temp = (a left rotate 5) + f + e + k + current word
        temp = bin(int(_left_rotate(a, 5), 2) + fk[0] + int(e,2) + fk[1] + int(word_list[i], 2))[2:]

        # Truncate left-most bits until temp is 32 bits long
        temp = _truncate(temp, 32)

        # Change the values of a, b, c, d, e for the next iteration
        e = d                   # e = d
        d = c                   # d = c
        c = _left_rotate(b, 30) # c = b left rotate 30
        b = a                   # b = a
        a = temp                # a = temp


    # 5 parts of the digest, which will be combined, unless they are longer than 32 bits each,
    # in which case they will be truncated first and then combined.
    global h0
    global h1
    global h2
    global h3
    global h4
    h0 = _truncate(bin(int(h0, 2) + int(a, 2))[2:], 32)
    h1 = _truncate(bin(int(h1, 2) + int(b, 2))[2:], 32)
    h2 = _truncate(bin(int(h2, 2) + int(c, 2))[2:], 32)
    h3 = _truncate(bin(int(h3, 2) + int(d, 2))[2:], 32)
    h4 = _truncate(bin(int(h4, 2) + int(e, 2))[2:], 32)
    
    # Convert 5 parts to hex and combine
    hh = hex(int(h0,2))[2:] + hex(int(h1,2))[2:] + hex(int(h2,2))[2:] + hex(int(h3,2))[2:] + hex(int(h4,2))[2:]

    return hh


    



def _f1(word):

    global a
    global b
    global c
    global d

    # f = (b AND c) OR (!b AND c)
    f = (int(b,2) & int(c,2)) | ((~int(b,2)) & int(d,2))

    k = int("01011010100000100111100110011001", 2)

    return f, k



def _f2(word):

    global a
    global b
    global c
    global d

    # f = b XOR c XOR d
    f = int(b,2) ^ int(c,2) ^ int(d,2)

    k = int("01101110110110011110101110100001", 2)

    return f, k



def _f3(word):

    global a
    global b
    global c
    global d

    # f = (b AND c) OR (b AND d) OR (c AND d)
    f = (int(b,2) & int(c,2)) | (int(b,2) & int(d,2)) | (int(c,2) & int(d,2))

    k = int("10001111000110111011110011011100", 2)

    return f, k



def _f4(word):

    global a
    global b
    global c
    global d

    # f = b XOR c XOR d
    f = int(b,2) ^ int(c,2) ^ int(d,2)

    k = int("11001010011000101100000111010110", 2)
    
    return f, k




def _left_rotate(binary_string, amount):

    temp = binary_string[:amount]
    binary_string = binary_string[amount:] + temp
    return binary_string



# Truncates from the left
def _truncate(binary_string, desired_amount):

    if len(binary_string) < desired_amount:
        raise ValueError("Could not truncate {} -- desired amount \"{}\" is greater than length of binary string ({})".format(binary_string, desired_amount,
                                                                                                                              str(len(binary_string))))

    return binary_string[len(binary_string)-desired_amount:]

