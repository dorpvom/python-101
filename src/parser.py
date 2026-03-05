# generally just google python 3 <what i want to do>, works mostly
# specifically look at https://docs.python.org/3/library/functions.html

import os
import sys
import argparse
import pathlib

def process_args():
    parser = argparse.ArgumentParser(
        prog = "CSV Parser",
        description = "Why do I even do this myself? There are plenty of libraries",
    )
    parser.add_argument("path", type=pathlib.Path)

    return parser.parse_args()

def read_data(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data

def print_dict(csv_dict):

    header = csv_data.pop(0)
    format_string = "{}\t" + "".join(map(lambda header_name: "{}: {{}}\t\t".format(header_name), header))


    for line_number, values in csv_data.items():
        print(format_string.format(line_number, *values))

if __name__ == "__main__":

    args = process_args()

    data = read_data(args.path)

    if not data:
        print("Empty file")
        sys.exit(1)

    csv_data = {}
    for i, line in enumerate(data.splitlines(keepends=False)):
        values = line.split(",")
        csv_data[i] =  list(map(lambda x: x.strip(), values))

    if not csv_data:
        print("Empty file")
        sys.exit(1)

    print_dict(csv_data)
