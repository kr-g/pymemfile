
# Changelog


## next release v0.0.2

- open function with parameters
- changed open behaviour slightly since call open in `with` context
 raised `FileAlreadyOpen`

usage before:

    with mf:
        mf.write(...)
        
usage after:
    
    file = MemFile("test.file","w")
    with file.open() as mf:
        mf.write(...)

or:

    with MemFile("test.file","w").open() as mf:
        mf.write(...)

or:

    with MemFile().open("test.file","w") as mf:
        mf.write(...)



## release v0.0.1

- first release
