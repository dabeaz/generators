# apachelog.py
#
# Parse an apache log file into a sequence of dictionaries

from fieldmap import field_map

import re

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = re.compile(logpats)

def apache_log(lines):
    groups = (logpat.match(line) for line in lines)
    tuples = (g.groups() for g in groups if g)
    
    colnames = ('host','referrer','user','datetime',
                'method', 'request','proto','status','bytes')

    log      = (dict(zip(colnames,t)) for t in tuples)
    log      = field_map(log,"status",int)
    log      = field_map(log,"bytes",
                         lambda s: int(s) if s != '-' else 0)

    return log

# Example use:

if __name__ == '__main__':
    from linesdir import lines_from_dir
    lines = lines_from_dir("access-log*","www")
    log = apache_log(lines)
    for r in log:
        print(r)


