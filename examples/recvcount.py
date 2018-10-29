# recvcount.py
#
# Example of a co-routine

def recv_count():
    try:
        while True:
            n = (yield)
            print("T-minus", n)
    except GeneratorExit:
        print("Kaboom!")

r = recv_count()
r.send(None)
for i in range(5,0,-1):
    r.send(i)

r.close()

