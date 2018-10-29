# receivefrom.py
#
# Receive objects from a different machine

import socket
from genpickle import gen_unpickle

def receivefrom(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    c, a = s.accept()
    for item in gen_unpickle(c.makefile('rb')):
        yield item
    c.close()

# Example use:
if __name__ == '__main__':
    for r in receivefrom(("",15000)):
        print(r['host'], r['request'])
