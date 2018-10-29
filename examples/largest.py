# largest.py
#
# Find the largest file

from linesdir import lines_from_dir
from apachelog import apache_log

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

print("%d %s" % max((r['bytes'],r['request'])
                    for r in log))
