# genpickle.py
#
# Turn a sequence of objects into a sequence of pickle strings

import pickle

def gen_pickle(source):
    for item in source:
        yield pickle.dumps(item)

def gen_unpickle(infile):
    while True:
        try:
            item = pickle.load(infile)
            yield item
        except EOFError:
            return

