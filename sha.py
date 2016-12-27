from expand_chunk import expand_chunk
from digest import digest


def sha(message):

    # 64-bit binary string of the amount of bits in the original message
    message_length = bin(len(message) * 8)[2:].zfill(64)


    # Convert inputted message to binary
    bin_message = _ascii_to_bin(message)

    
    # Append 1 to binary message
    bin_message += "1"
    

    # Pad binary number with zeros until its length is congruent to 448 mod 512
    amount_zeros = 448 - (len(bin_message) % 512)
    for i in range(amount_zeros):
        bin_message += "0"


    # Append the 64-bit length of original message.
    # Message length in bits should now be a multiple of 512.
    bin_message += message_length


    # Break binary message up into 512 bit chunks
    chunk_list = []
    for i in range(0, len(bin_message), 512):
        chunk_list.append(bin_message[i:i+512])


    # Get the word list for each chunk, and store it in wordlist_list (list of lists)
    wordlist_list = []
    for chunk in chunk_list:
        wordlist_list.append(expand_chunk(chunk))


    # Digest all chunks and return the result
    h_list = ["01100111010001010010001100000001", "11101111110011011010101110001001",
              "10011000101110101101110011111110", "00010000001100100101010001110110",
              "11000011110100101110000111110000"]
    for wordlist in wordlist_list:
        h_list = digest(wordlist, h_list)


    # Create final hash by combine the parts in h_list
    hh = ""
    for h in h_list:
        hh += hex(int(h,2))[2:].zfill(8)

    
    return hh


        

    



def _ascii_to_bin(text):

    out = ""
    for letter in text:
        out += bin(ord(letter))[2:].zfill(8)

    return out
