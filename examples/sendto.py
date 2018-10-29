# sendto.py
#
# Send items to a remote machine

import socket
from genpickle import gen_pickle

def sendto(source,addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(addr)
    for pitem in gen_pickle(source):
        s.sendall(pitem)
    s.close()

# Example use.   This requires you to run receivefrom.py
# in a different process/window

if __name__ == '__main__':
    from apachelog import apache_log
    from follow import follow

    lines = follow(open("run/foo/access-log"))
    log = apache_log(lines)
    sendto(log,("",15000))

