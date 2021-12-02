import os, sys

if len(sys.argv) < 1:
    print("provide day number!")
    sys.exit(1)

path = "day" + sys.argv[1]

try:
    os.mkdir(path)
    open(path+"/day"+sys.argv[1]+".py", "a")
    open(path+"/input"+sys.argv[1]+".txt", "a")
    open(path+"/example"+sys.argv[1]+".txt", "a")
except OSError:
    print("Creation of", path, "failed!")
else:
    print("Created", path, "!")
