# gentrace.py
#
# Trace a generator by printing items received

def trace(source):
    for item in source:
        print(item)
        yield item

# Example use
if __name__ == '__main__':
    from apachelog import *

    lines = open("access-log")
    log =  trace(apache_log(lines))
    r404 = (r for r in log if r['status'] == 404)

    for r in r404:
        pass


                
