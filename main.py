from flatten_array import flatten_array
from Temperatures import TemperaturesHandler
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')
    subparsers.required = True

    parser_a = subparsers.add_parser('flatten_array')
    parser_a.add_argument('-a', '--array', required=True)

    parser_b = subparsers.add_parser('temperatures')
    parser_b.add_argument('-f', '--file', required=True)
    parser_b.add_argument('-fn', '--function', required=True)
    parser_b.add_argument('-r', '--ranges', required=False)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # parse arguments
    args = parse_args()
    if args.action == 'flatten_array':
        arr = json.loads(args.array)
        result_array = flatten_array(arr)
        print(result_array)
    else:
        file = args.file
        temperatures_handler = TemperaturesHandler(file)
        if args.function == "lowest":
            print(temperatures_handler.lowest_temperature())
        elif args.function == "lf_dates":
            if args.ranges:
                print(temperatures_handler.largest_fluctuation_station_by_dates(json.loads(args.ranges)))

