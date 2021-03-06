from pymemfile import MemFile

file = MemFile("test.file", "r+")
print(file)

with file.open() as mf:

    mf.write("hello ")
    mf.write("world\n")

    print("-have a nice day-", file=mf.fileno())
    print()

    print("cur position", mf.tell())

    mf.seek(0)
    print(mf.read())

    mf.seek(5)
    mf.write(" test ")
    mf.seek(0)
    print(mf.read())


mf.open()
print("---")
print(mf.read())
mf.close()
