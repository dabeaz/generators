# gencat.py
#
# Concatenate multiple generators into a single sequence

def gen_cat(sources):
    for src in sources:
        yield from src

# Example use

if __name__ == '__main__':
    from pathlib import Path
    from genopen import gen_open

    lognames = Path('www').rglob('access-log*')
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)
    for line in loglines:
        print(line,end='')
