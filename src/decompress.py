
def decompress(compressed):

    output = ""

    for value in compressed:
        offset, length, char = value

        if length == 0:
            if char is not None:
                output += char
        else:
            if offset == 0:
                if char is not None:
                    output += char
                    length -= 1
                    offset = 1
            start_index = len(output) - offset
            for i in range(length):
                output += output[start_index + i]
    return output

def from_bytes(compressed_bytes):

    offset_bits = 11
    length_bits = 5
    offset_length_bytes = int((offset_bits + length_bits) / 8)
    output = []

    while len(compressed_bytes) > 0:
        offset_length_value = 0
        for _ in range(offset_length_bytes):
            offset_length_value = offset_length_value * 256 + int(compressed_bytes.pop(0))

        offset = offset_length_value >> length_bits
        length = offset_length_value & ((2 ** length_bits) - 1)

        if offset > 0:
            char_out = None
        else:
            char_out = str(chr(compressed_bytes.pop(0)))

        output.append((offset, length, char_out))
    return output

if __name__ == "__main__":

    pass
