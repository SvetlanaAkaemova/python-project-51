import argparse
import os


def parser_args():
    parser = argparse.ArgumentParser(
        description='Downloads the page to the specified directory.'
    )
    parser.add_argument('page_url')
    parser.add_argument(
        '-o', '--output', default=os.getcwd(),
        help='specified directory for download page'
    )
    args = parser.parse_args()
    return args
