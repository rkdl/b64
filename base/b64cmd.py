from argparse import ArgumentParser

from base_velosiped import to_base64, base64_decode


def parse_cmd_args():
    parser = ArgumentParser()
    parser.add_argument('file', type=str)
    parser.add_argument(
        '-D', dest='decode', action='store_true', help='decode mode'
    )
    return parser.parse_args()


def main():
    args = parse_cmd_args()
    with open(args.file, 'rb') as f:
        bts = f.read()
    converted = base64_decode(bts) if args.decode else to_base64(bts)
    output = converted.decode('utf8')
    print(output)


if __name__ == '__main__':
    main()
