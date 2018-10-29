# query404.py
#
# Find the set of all documents that 404 in a log file

from linesdir import lines_from_dir
from apachelog import apache_log

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

stat404 =  {  r['request'] for r in log
              if r['status'] == 404 }

for r in sorted(stat404):
    print(r)
