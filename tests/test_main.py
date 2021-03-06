import io

import json

from pymemfile import MemFile
from pymemfile.file import FileAlreadyOpenError, FileNotOpenError, FileReadOnlyError


import unittest


class MemFile_TestCase(unittest.TestCase):
    def test_not_open(self):

        mf = MemFile("test.file", "r")
        print(mf)

        self.assertRaises(
            FileNotOpenError,
            mf.read,
        )

    def test_reopen(self):

        mf = MemFile("test.file", "r+")
        mf.open()

        self.assertRaises(
            FileAlreadyOpenError,
            mf.open,
        )

    def test_readonly(self):

        mf = MemFile("test.file", "r")
        mf.open()

        self.assertRaises(FileReadOnlyError, mf.write, data="hello")

    def test_with(self):

        test_data = "hello\tworld!\n"

        file = MemFile("test.file", "r+")
        with file.open() as mf:
            mf.write(test_data)

        self.assertRaises(FileNotOpenError, mf.write, test_data)

    def test_seek_tell(self):

        test_data = "hello\tworld!\n"

        file = MemFile("test.file", "r+")
        with file.open() as mf:
            mf.write(test_data)
            mf.seek(0)
            cnt = mf.read()
            self.assertEqual(cnt, test_data)

            pos = mf.tell()
            self.assertEqual(pos, len(test_data))

    def test_open_append(self):

        test_data = "hello\tworld!\n"

        file = MemFile("test.file", "r+a")

        with file.open() as mf:
            mf.write(test_data)

        with file.open() as mf:
            pos = mf.tell()
            self.assertEqual(pos, len(test_data))

    def test_open_overwrite(self):

        test_data = "hello\tworld!\n"

        file = MemFile("test.file", "w")

        with file.open() as mf:
            mf.write(test_data)
            pos = mf.tell()
            self.assertEqual(pos, len(test_data))

        with file.open() as mf:
            pos = mf.tell()
            self.assertEqual(pos, 0)

    def test_open_parameter(self):

        test_data = "hello\tworld!\n"

        file = MemFile()

        with file.open("test.file", "w") as mf:
            mf.write(test_data)
            pos = mf.tell()
            self.assertEqual(pos, len(test_data))

    def test_open_parameter_in_place(self):

        test_data = "hello\tworld!\n"

        with MemFile().open("test.file", "w") as mf:
            mf.write(test_data)
            pos = mf.tell()
            self.assertEqual(pos, len(test_data))

        self.assertFalse(mf._open)
