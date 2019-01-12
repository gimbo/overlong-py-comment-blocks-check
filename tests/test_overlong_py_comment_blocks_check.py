import pytest

from overlong_py_comment_blocks_check import overlong_py_comment_blocks_check
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('test_subject', 'threshold', 'expected_return_value', 'blocks'), (
        ('empty_file', 1, 0, ()),
        ('no_comments', 1, 0, ()),
        ('comment_block_only', 1, 1, ((1, 3),)),
        ('comment_block_only', 4, 0, ()),
        ('one_comment_block', 3, 1, ((7, 3),)),
        ('one_comment_block', 10, 0, ()),
        ('several_long_blocks', 3, 1, ((5, 3), (11, 8), (24, 7))),
        ('several_long_blocks', 5, 1, ((11, 8), (24, 7))),
        ('several_long_blocks', 10, 0, ()),
    ),
)
def test_overlong_blocks(
    capsys,
    test_subject,
    threshold,
    expected_return_value,
    blocks,
):
    filename = test_subject + '.py'
    args = [
        '--threshold={}'.format(threshold),
        get_resource_path(filename),
    ]
    return_value = overlong_py_comment_blocks_check.main(args)
    assert return_value == expected_return_value
    if expected_return_value == 1:
        stdout, _ = capsys.readouterr()
        for line, (start, length) in zip(stdout.split('\n'), blocks):
            assert '{}-line'.format(length) in line
            assert '{} in'.format(start) in line
            assert filename in line


@pytest.mark.parametrize(('threshold'), (0, -1, -10))
def test_bad_threshold(capsys, threshold):
    args = [
        '--threshold={}'.format(threshold),
        'some_path',
    ]
    with pytest.raises(SystemExit):
        overlong_py_comment_blocks_check.main(args)
    stdout, stderr = capsys.readouterr()
    assert not stdout
    assert 'invalid positive int value: {}'.format(threshold) in stderr
