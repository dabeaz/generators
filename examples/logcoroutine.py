# logcoroutine.py
#
# An example of using co-routines to define consumers for the Apache log data

from consumer import *
from apachelog import *
from follow import *
from broadcast import *

@consumer
def find_404():
    while True:
        r = (yield)
        if r['status'] == 404:
            print(r['status'],r['datetime'],r['request'])

@consumer
def bytes_transferred():
    total = 0
    while True:
        r = (yield)
        total += r['bytes']
        print("Total bytes", total)

lines = follow(open("run/foo/access-log"))
log   = apache_log(lines)

broadcast(log, [find_404(),bytes_transferred()])
