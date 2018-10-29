# Make a big log file for testing

import sys

if len(sys.argv) != 2:
    print("Usage : makebig.py repetitions", file=sys.stderr)
    raise SystemExit(1)

data = open("access-log").read()

with open("big-access-log","w") as f:
    for i in range(int(sys.argv[1])):
        f.write(data)




    
