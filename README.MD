
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# pymemfile - in memory file

based on python stream classes this behaves like a file but with no persistence on a hard drive


supported methods:

- read
- write
- seek
- tell
- fileno
- with context
- 


# how to use

refer to [`sample.py`](https://github.com/kr-g/pymemfile/blob/main/sample.py)

code:

    from pymemfile import MemFile

    mf = MemFile("test.file", "r+")
    print(mf)

    with mf:

        mf.write("hello ")
        mf.write("world\n")

        print("-have a nice day-", file=mf.fileno())
        print()
        
        print("cur position", mf.tell())

        mf.seek(0)
        print(mf.read())


# Platform

Tested on Python3, and Linux.


# Development status

alpha state.
the API or logical call flow might change without prior notice.

read [`CHANGELOG`](https://github.com/kr-g/pymemfile/blob/master/CHANGELOG.MD)
for latest, or upcoming news.


# installation
    
available on pypi. install with:

    python3 -m pip install pymemfile
    
