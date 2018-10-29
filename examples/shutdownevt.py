# shutdownevt.py
#
# Example of a generator that uses an event to shut down

import time

def follow(thefile,shutdown=None):
    thefile.seek(0,2)
    while True:
        if shutdown and shutdown.isSet(): break
        line = thefile.readline()
        if not line:
           time.sleep(0.1)
           continue
        yield line

import threading

shutdown_event = threading.Event()

def run():
    lines = follow(open("run/foo/access-log"),shutdown_event)
    for line in lines:
        print line,

    print "Done"


# Run the above in a separate thread
t = threading.Thread(target=run)
t.start()

# Wait a while then shut down


time.sleep(60)
print "Shutting down"

shutdown_event.set()

