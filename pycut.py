import argparse
import sys

def process_line(line, fields_indexes, delimiter):
    fields = line.strip().split(delimiter)
    selected_fields = [fields[i] for i in fields_indexes if i < len(fields)]
    return delimiter.join(selected_fields)

def cut(file_path, fields_indexes, delimiter):
    with open(file_path, 'r') if file_path and file_path != '-' else sys.stdin as file:
        for line in file:
            print(process_line(line, fields_indexes, delimiter))

def parse_arguments():
    parser = argparse.ArgumentParser(description="A Python implementation of the Unix cut command.")
    parser.add_argument('-f', '--fields', required=True, help="Comma-separated list of fields to be selected.")
    parser.add_argument('-d', '--delimiter', default='\t', help="Delimiter character.")
    parser.add_argument('file', nargs='?', help="File to process. Reads from stdin if omitted or if '-' is provided.")
    return parser.parse_args()

def main():
    args = parse_arguments()
    fields_indexes = [int(f) - 1 for f in args.fields.split(',')]
    cut(args.file, fields_indexes, args.delimiter)

if __name__ == "__main__":
    main()
