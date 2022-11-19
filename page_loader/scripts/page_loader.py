#!usr/bin/env python3
from page_loader import download
from page_loader.modules.parser_args import parser_args


def main():
    args = parser_args()
    print(download(args.page_url, directory=args.output))


if __name__ == '__main__':
    main()
