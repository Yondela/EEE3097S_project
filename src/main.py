from compress import compression, to_bytes
from decompress import decompress, from_bytes

def read_data(filename):
    """This function is used to read the contents of the file."""

    with open(filename, 'r') as f:

        return f.readlines()
        #return f.read()

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

if __name__ == "__main__":

    #print( to_bytes(compression(read_data("data/2018-09-19-03_57_11_VN100.csv"))) )
    #print(read_data("data/2018-09-19-03_57_11_VN100.csv"))

    lines_compressed = []

    for i in read_data("data/2018-09-19-03_57_11_VN100.csv"):

        lines_compressed.append(to_bytes(compression(i)))

    for i in lines_compressed:

        print(i)
        print(decompress(from_bytes(i)))
