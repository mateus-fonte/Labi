import hashlib
from os import readlink
import sys

 
h = hashlib.sha1()
def fun(file):
    with open(file, 'rb') as f:
        buffer = f.read(512)
        while len(buffer) > 0:
            buffer = f.read(512)
            h.update(buffer)
    return h.hexdigest()
pai = fun(sys.argv[0])
print(pai)