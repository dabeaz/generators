import subprocess
import time

print "Running simulated web servers"
print 
print "This runs a simulated server that writes these log files"
print
print "    run/foo/access-log"
print "    run/bar/access-log"
print
print "Please leave this running as a background process while"
print "working on examples related to infinite input streams"

p1 = subprocess.Popen(['python','logsim.py'],
                      cwd='run/foo')

time.sleep(600)
p2 = subprocess.Popen(['python','logsim.py'],
                      cwd='run/bar')

p1.wait()
p2.wait()
