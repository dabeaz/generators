# fieldmap.py
#
# Take a sequence of dictionaries and remap one of the fields

def field_map(dictseq, name, func):
    for d in dictseq:
        d[name] = func(d[name])
        yield d

# Example

if __name__ == '__main__':

    loglines = open("access-log")

    import re

    logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
               r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

    logpat   = re.compile(logpats)

    groups   = (logpat.match(line) for line in loglines)
    tuples   = (g.groups() for g in groups if g)

    colnames = ('host','referrer','user','datetime',
                'method', 'request','proto','status','bytes')

    log      = (dict(zip(colnames, t)) for t in tuples)

    log      = field_map(log,"status",int)
    log      = field_map(log,"bytes",
                         lambda s: int(s) if s != '-' else 0)

    
    for x in log:
        print(x)
