def digest(word_list, h):

    # Raise exception if input word_list does not have correct amount of words
    if len(word_list) != 80:
        raise ValueError("Inputted list of words must have 80 words, but instead has {} words".format(str(len(word_list))))

    a = h[0]
    b = h[1]
    c = h[2]
    d = h[3]
    e = h[4]
    
    
    # Determine which function to use depending on the posisition of the word in word_list
    for i in range(len(word_list)):

        if i <= 19:
            fk = _f1(word_list[i], a,b,c,d)

        elif i <= 39:
            fk = _f2(word_list[i], a,b,c,d)

        elif i <= 59:
            fk = _f3(word_list[i], a,b,c,d)

        else:
            fk = _f4(word_list[i], a,b,c,d)

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


    # 5 parts of the digest, which will be combined after each chunk in sha.py is digested
    h[0] = _truncate(bin(int(h[0], 2) + int(a, 2))[2:], 32)
    h[1] = _truncate(bin(int(h[1], 2) + int(b, 2))[2:], 32)
    h[2] = _truncate(bin(int(h[2], 2) + int(c, 2))[2:], 32)
    h[3] = _truncate(bin(int(h[3], 2) + int(d, 2))[2:], 32)
    h[4] = _truncate(bin(int(h[4], 2) + int(e, 2))[2:], 32)


    return h


    



def _f1(word, a, b, c, d):

    # f = (b AND c) OR (!b AND c)
    f = (int(b,2) & int(c,2)) | ((~int(b,2)) & int(d,2))

    k = int("01011010100000100111100110011001", 2)

    return f, k



def _f2(word, a, b, c, d):

    # f = b XOR c XOR d
    f = int(b,2) ^ int(c,2) ^ int(d,2)

    k = int("01101110110110011110101110100001", 2)

    return f, k



def _f3(word, a, b, c, d):

    # f = (b AND c) OR (b AND d) OR (c AND d)
    f = (int(b,2) & int(c,2)) | (int(b,2) & int(d,2)) | (int(c,2) & int(d,2))

    k = int("10001111000110111011110011011100", 2)

    return f, k



def _f4(word, a, b, c, d):

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
        return binary_string.zfill(desired_amount - len(binary_string))
  
    return binary_string[len(binary_string)-desired_amount:]
