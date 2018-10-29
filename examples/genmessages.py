# genmessages.py
#
# A generator that yields messages on a UDP socket

import socket
def receive_messages(addr,maxsize):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(addr)
    while True:
        msg = s.recvfrom(maxsize)
        yield msg

# Example use
# To send a message to this generator, use the code "msgtest.py"

if __name__ == '__main__':
    for msg, addr in receive_messages(("",10000),1024):
        print(msg, "from", addr)


    
