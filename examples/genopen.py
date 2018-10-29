# genopen.py
#
# Takes a sequence of filenames as input and yields a sequence of file
# objects that have been suitably open

import gzip, bz2

def gen_open(paths):
    for path in paths:
        if path.suffix == '.gz':
            yield gzip.open(path, 'rt')
        elif path.suffix == '.bz2':
            yield bz2.open(path, 'rt')
        else:
            yield open(path, 'rt')

# Example use

if __name__ == '__main__':
    from pathlib import Path
    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    for f in logfiles:
        print(f)
