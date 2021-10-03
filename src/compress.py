
def read_data(filename):
    """This function is used to read the contents of the file."""

    with open(filename, 'r') as f:

        #return f.readlines()
        return f.read()

def filenames():

    filenames = [ "2018-09-19-03_57_11_VN100.csv",
        "2018-09-19-04_22_21_VN100.csv",
        "2018-09-19-06_28_11_VN100.csv",
        "2018-09-19-06_53_21_VN100.csv",
        "2018-09-19-08_59_11_VN100.csv",
        "2018-09-19-09_24_21_VN100.csv",
        "2018-09-19-09_49_31_VN100.csv",
        "2018-09-19-11_55_21_VN100.csv",
        "2018-09-19-12_20_31_VN100.csv",
    ]

    return filenames

def compression(input_string):

    max_offset = 2047
    max_length = 31
    input_array = str(input_string[:])

    window = ""

    output = []

    while input_array != "":

        length, offset = best_length_offset(window, input_array, max_length, max_offset)
        output.append((offset, length, input_array[0]))
        window += input_array[:length]
        input_array = input_array[length:]

    return output

def to_bytes(compressed_representation):

    offset_bits = 11
    length_bits = 5

    output = bytearray()
    offset_length_bytes = int((offset_bits + length_bits) / 8)


    for value in compressed_representation:
        offset, length, char = value

        offset_length_value = (offset << length_bits) + length

        for count in range(offset_length_bytes):
            output.append((offset_length_value >> (8 * (offset_length_bytes - count - 1))) & (0b11111111))

        if char is not None:
            if offset == 0:
                output.append(ord(char))
        else:
            output.append(0)

    return output

def best_length_offset(window, input_string, max_length, max_offset):

    if max_offset < len(window):
        cut_window = window[-max_offset:]
    else:
        cut_window = window

    if input_string is None or input_string == "":
        return (0, 0)

    length, offset = (1, 0)

    if input_string[0] not in cut_window:
        best_length = repeating_length_from_start(input_string[0], input_string[1:])
        return (min((length + best_length), max_length), offset)

    length = 0

    for i in range(1, len(cut_window) + 1):
        char = cut_window[-i]
        if char == input_string[0]:
            found_offset = i
            found_length = repeating_length_from_start(cut_window[-i:], input_string)
            if found_length > length:
                length = found_length
                offset = found_offset
    return (min(length, max_length), offset)

def repeating_length_from_start(window, input_string):

    if window == "" or input_string == "":
        return 0

    if window[0] == input_string[0]:
        return 1 + repeating_length_from_start(window[1:] + input_string[0], input_string[1:]) 
    #else:
    return 0



if __name__ == "__main__":

    pass
