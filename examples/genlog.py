# genlog.py
#
# Sum up the bytes transferred in an Apache server log using
# generator expressions

with open("access-log") as wwwlog:
    bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
    bytes_sent = (int(x) for x in bytecolumn if x != '-')
    print("Total", sum(bytes_sent))
