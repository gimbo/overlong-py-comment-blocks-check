from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

import argparse
import io
import re


DEFAULT_THRESHOLD = 20


def main(argv=None):
    args = parse_args(argv)
    dirtiness_results = {
        check_and_report_overlong_py_comment_blocks(filename, args.threshold)
        for filename in args.filenames
    }
    return 0 if dirtiness_results == {False} else 1


def check_and_report_overlong_py_comment_blocks(path, threshold):
    dirties = find_overlong_py_comment_blocks(path, threshold)
    for start, length in dirties:
        print(
            '* {:>3}-line comment block at line {:>5} in {}'.format(
                length,
                start,
                path,
            )
        )
    return bool(dirties)


def find_overlong_py_comment_blocks(path, threshold):
    # We build a string of first letters of lines (using a space to
    # represent an empty line), split that on comment blocks, and
    # return starts and lengths of long blocks.
    firsts = first_chars_of_stripped_lines_from_file_as_a_string(path)
    # Add 1 here because the string we're working on is 0-indexed but
    # line numbers in a file are, by convention, 1-indexed.
    comment_blocks = (
        (match.start() + 1, match.end() - match.start())
        for match in re.finditer('(#+)', firsts)
    )
    return [
        (start, length)
        for start, length in comment_blocks
        if length >= threshold
    ]


def first_chars_of_stripped_lines_from_file_as_a_string(path):
    with io.open(path, encoding='utf-8') as infile:
        stripped = [line.lstrip() for line in infile]
    return ''.join(
        [line[0] if line else ' ' for line in stripped]
    )


def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    parser.add_argument(
        '--threshold', '-t',
        type=positive_int,
        default=DEFAULT_THRESHOLD,
        metavar='LINES',
        help="""
            How long must a comment block be (in lines) for it to be
            too long.  Default: {}
        """.format(DEFAULT_THRESHOLD),
    )
    return parser.parse_args(argv)


def positive_int(x):
    """Argument value parser: positive integers."""
    try:
        n = int(x)
        if n <= 0:
            raise ValueError()
        return n
    except ValueError:
        raise argparse.ArgumentTypeError(
            'invalid positive int value: {}'.format(x),
        )


if __name__ == '__main__':
    exit(main())
