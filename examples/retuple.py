# retuple.py
#
# Read a sequence of log lines and parse them into a sequence of tuples

loglines = open("access-log")

import re

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = re.compile(logpats)

groups   = (logpat.match(line) for line in loglines)
tuples   = (g.groups() for g in groups if g)

if __name__ == '__main__':
    for t in tuples:
        print(t)
