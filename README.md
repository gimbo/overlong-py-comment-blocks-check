[![Build Status](https://travis-ci.org/gimbo/overlong-py-comment-blocks-check.svg?branch=master)](https://travis-ci.org/gimbo/overlong-py-comment-blocks-check)
[![Coverage Status](https://coveralls.io/repos/github/gimbo/overlong-py-comment-blocks-check/badge.svg?branch=master)](https://coveralls.io/github/gimbo/overlong-py-comment-blocks-check?branch=master)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/sl3kkmimf4t1h9pn?svg=true)](https://ci.appveyor.com/project/gimbo/overlong-py-comment-blocks-check)


# overlong-py-comment-blocks-check

This is a pre-commit hook, written for the [pre-commit.com
framework](https://pre-commit.com/), which looks for python modules
containing suspiciously long comment blocks (i.e. blocks of code all
of whose lines begin with the "`#`" character, ignoring leading
whitespace).

The motivation is to help with looking for dead/old/commented out code
in a large codebase.

## Configuration

Example `.pre-commit-config.yaml` entry:

      - repo: https://github.com/gimbo/overlong-py-comment-blocks-check.git
        rev: master
        hooks:
          - id: overlong-py-comment-blocks-check
            args: [--threshold=10]

The `threshold` argument controls how long a block must be (in lines)
in order to be considered a problem; the default is 20.

## Future work

* Possibly: a way to mark a given block so that it's ignored by this
  check.
