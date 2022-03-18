import hashlib
import sys

h = hashlib.sha1()
with open(sys.stdin.fileno(), "rb") as f:
    while True:
        buffer = f.read(1024)
        if len(buffer) == 0:
            break
        h.update(buffer)
print(h)
