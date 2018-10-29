# broadcast.py
#
# Broadcast a generator source to a collection of consumers

def broadcast(source, consumers):
    for item in source:
        for c in consumers:
            c.send(item)


# Example
if __name__ == '__main__':

    class Consumer(object):
        def send(self,item):
            print(self, "got", item)

    c1 = Consumer()
    c2 = Consumer()
    c3 = Consumer()

    from follow import follow
    lines = follow(open("run/foo/access-log"))
    broadcast(lines,[c1,c2,c3])

