# genevents.py
#
# A very simplistic example of generating events on a set of sockets

import select
def gen_events(socks):
    while True:
        rdr,wrt,err = select.select(socks,socks,socks,0.1)
        for r in rdr:
            yield "read",r
        for w in wrt:
            yield "write",w
        for e in err:
            yield "error",e

# Example use
# Use telnet to port 12000 to test this

if __name__ == '__main__':
    import socket
    from genreceive import *

    addr = ("",12000)
    clientset = []
    def acceptor(sockset,addr):
        for c,a in receive_connections(addr):
            clientset.append(c)

    import threading
    acc_thr = threading.Thread(target=acceptor,
                               args = (clientset, addr))
    acc_thr.daemon = True
    acc_thr.start()
    
    for evt, s in gen_events(clientset):
        if evt == 'read':
            data = s.recv(1024)
            if not data:
                print("Closing", s)
                s.close()
                clientset.remove(s)
            else:
                print(s,data)




