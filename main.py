import argparse

from tools import profit
from tools import table

def main(args):
    input = args.input

    record = table.Record()
    record.show()
    # record.register()
    record.show()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    args = parser.parse_args()
    main(args)
