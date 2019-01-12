from setuptools import (
    find_packages,
    setup,
)


setup(
    name='overlong-py-comment-blocks-check',
    description=(
        "pre-commit hook: check that python modules don't contain long "
        "comment blocks which might be commented out code"
    ),
    url='https://github.com/gimbo/overlong-py-comment-blocks-check',
    version='1.0.0',

    author='Andy Gimblett',
    author_email='gimbo@gimbo.org.uk',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'overlong-py-comment-blocks-check = overlong_py_comment_blocks_check.overlong_py_comment_blocks_check:main',
        ],
    },
)
