# io_utilities.py

def read_vanilla(filepath):
    filepath = './data/iris.data'

    with open(filepath,'r') as fp:
        data = fp.read()

    data_lines = data.split('\n')

    data_final = [f.split(',') for f in data_lines]

    return data_final
