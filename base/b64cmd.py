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
    bts = bytes(args.file, 'utf8')
    if args.decode:
        print(base64_decode(bts).decode('utf8'))
    else:
        print(to_base64(bts))


if __name__ == '__main__':
    main()
