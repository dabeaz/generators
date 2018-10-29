# gengrep.py
#
# Grep a sequence of lines that match a re pattern

import re
def gen_grep(pat, lines):
    patc = re.compile(pat)
    return (line for line in lines if patc.search(line))

# Example use

if __name__ == '__main__':
    from pathlib import Path
    from genopen import  gen_open
    from gencat  import  gen_cat

    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)

    # Look for ply downloads (PLY is my own Python package)
    plylines = gen_grep(r'ply-.*\.gz',loglines)
    for line in plylines:
        print(line, end='')
