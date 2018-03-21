from __future__ import division
import numpy as np


def length_hist(bit_stream):
    """Return a histogram of the number of consecutive bits in a bit stream"""
    print(bit_stream)
    hist = {}
    current_len = 1
    min_len = 10000

    for i in range(1, len(bit_stream[:])):
        if bit_stream[i-1] == bit_stream[i]:
            current_len += 1
        else:
            if hist.get(current_len) is None:
                hist[current_len] = 1
            else:
                hist[current_len] = hist[current_len] + 1
            if current_len < min_len:
                min_len = current_len
            current_len = 1

    if hist.get(current_len) is None:
        hist[current_len] = 1
    else:
        hist[current_len] = hist[current_len] + 1
    return hist, min_len


def average_ratio(hist, min_len):
    num, total = 0, 0
    for k, v in hist.items():
        if (k-min_len) <= 2: # For all lengths within 2 of minimum width
            num += 1. * k * v 
            total += v
    return 1.0 * num / total


def get_majority(bits):
    ones = 0
    zeros = 0
    for bit in bits:
        if bit == '0':
            zeros += 1
        else:
            ones += 1
    return 1 if ones > zeros else 0


def calibrate_protocol(bit_stream):
    hist, min_len = length_hist(bit_stream)
    ratio = average_ratio(hist, min_len)
    return ratio, hist


def next_byte(ratio, min_len, testing_iter=None):
    while True:
        ignored_bits = ''
        # Wait until a '\x00' char to start reading data
        # Wait until a 0 bit is read
        next_bit = '1'
        while next_bit == '1':
            if testing_iter is None:
                next_bit = str(rgpio.read(15)) # TODO: Change this line
            else:
                try:
                    next_bit = str(next(testing_iter))
                except StopIteration:
                    return
            ignored_bits += str(next_bit)

        # Wait till length of current_bits is long enough for 7 real bits
        current_bits = '0'
        while True:
            if testing_iter is None:
                next_bit = str(rgpio.read(15)) # TODO: Change this line
            else:
                try:
                    next_bit = str(next(testing_iter))
                except StopIteration:
                    return
            ignored_bits += str(next_bit)
            current_bits += str(next_bit)
            if next_bit == 1:
                current_bits = ''
            if len(current_bits) > int(7*ratio) + 1:
                break

        if testing_iter is not None:
            print('Ignored bits are:', ignored_bits)
        # Start reading next byte
        while True:
            if testing_iter is not None:
                print('Getting next byte:')
                print('Bits are: \'', end='')
            byte = ''
            current_bits = '0'
            # Read rest of bits
            count = 0
            while True:
                # Read bit (either till switch or min_length + 1 times)
                if testing_iter is None:
                    next_bit = str(rgpio.read(15)) # TODO: Change this line
                else:
                    try:
                        next_bit = str(next(testing_iter))
                    except StopIteration:
                        return
                    print(next_bit, end='')

                if next_bit != current_bits[-1]: # Switch
                    # Get the number of bits written 
                    num_bits = int(round(len(current_bits) / ratio))
                    for i in range(num_bits):
                        byte += current_bits[-1]
                    current_bits = ''
                current_bits += next_bit

                if len(byte) >= 6:
                    break


            if testing_iter is not None:
                print('\nRead bits are:', byte)
            byte = chr(int(byte, 2))
            if testing_iter is not None:
                print('Ascii is:', byte)
            yield byte


def generate_fake_message(msg, ratio=4.5):
    binary_msg = ''
    prev_ind = 0
    for char in msg:
        print("Char {}, ascii {}, bin {}".format(char, ord(char), bin(ord(char))))
        for bit in bin(ord(char))[2:]:
            current_ind = prev_ind + ratio
            bits = ''
            for _ in range(int(prev_ind), int(current_ind)):
                bits += bit
            binary_msg += bits
            prev_ind = current_ind
    return binary_msg


def test_protocol():
    # Create a message to encode and decode
    msg = 'This is the test message'
    # Message with '\0' character at the start
    binary_msg = '0000000'+'0000000'+'0000000'+'0000000'+'0000' + generate_fake_message(msg)
    print(binary_msg)
    
    # Iterator to send a bit at a time
    def msg_iter(msg=binary_msg):
        for bit in msg:
            yield bit
    testing_iter = msg_iter()

    # Recreate the message
    re_created_msg = ''
    for _ in range(18):   
        try:
            re_created_msg += next(next_byte(4.5, 4, testing_iter=testing_iter))
        except StopIteration:
            print('')
            
    print(re_created_msg)


if __name__ == '__main__':
    test_protocol()
