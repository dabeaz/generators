# genqueue.py
#
# Generate a sequence of items that put onto a queue

def genfrom_queue(thequeue):
    while True:
        item = thequeue.get()
        if item is StopIteration: 
            break
        yield item

def sendto_queue(items, thequeue):
    for item in items:
        thequeue.put(item)
    thequeue.put(StopIteration)

# Example
if __name__ == '__main__':
    import queue, threading
    def consumer(q):
        for item in genfrom_queue(q):
            print("Consumed", item)
        print("done")

    in_q = queue.Queue()
    con_thr = threading.Thread(target=consumer,args=(in_q,))
    con_thr.start()

    # Now, pipe a bunch of data into the queue
    sendto_queue(range(100), in_q)


