# genshutdown.py
#
# Example of shutting down a generator
#
# Requires you to run run/foo/logsim.py to get a real-time source

from follow import *

lines = follow(open("run/foo/access-log"))
for i, line in enumerate(lines):
    print(line, end='')
    if i == 10: 
        lines.close()
