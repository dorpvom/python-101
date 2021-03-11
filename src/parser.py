import argparse
import os
import sys
from pathlib import Path

def parse_row(csv_row, delim_char=','):
    return [value.strip() for value in csv_row.split(delim_char)]

def get_row_format(index: int, row_values: list, header: list) -> str:
    field_value_pairs = "\t".join([f"{field}: {value}" for field, value in  zip(header, row_values)])
    return f"{index}\t{field_value_pairs}"

def main(args):
    try:
        with open(args.file, 'r') as f:
            csv_rows = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return 1
    except IsADirectoryError:
        print("File is a directory")
        return 2

    parsed_rows = list(map(parse_row, csv_rows))
    header = parsed_rows.pop(0)
    for index, row_values in enumerate(parsed_rows):
        print(get_row_format(index, row_values, header))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file',
                        type=Path,
                        help='path to CSV file')
    args = parser.parse_args()
    sys.exit(main(args))

