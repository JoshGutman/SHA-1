from expand_chunk import expand_chunk
from digest import digest


def sha(message):

    # 64-bit binary representation of the length of the original message
    message_length = bin(len(message))[2:].zfill(64)


    # Convert inputted message to binary
    bin_message = _ascii_to_bin(message)

    
    # Append 1 to binary number
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
    hashes = []
    for wordlist in wordlist_list:
        hh = digest(wordlist)
        hashes.append(hh)


    return hashes


        

    



def _ascii_to_bin(text):

    out = ""
    for letter in text:
        out += bin(ord(letter))[2:].zfill(8)

    return out
