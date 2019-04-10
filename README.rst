Generator Tricks for Systems Programming (Tutorial)
===================================================

| Copyright (C) 2008, 2018
| David M. Beazley
| http://www.dabeaz.com

Originally Presented at PyCon 2008, March 13, 2008, Chicago, Illinois.

Revised and updated for Python 3.7, October 29, 2018.

Introduction
------------

This tutorial discusses various techniques for using generator
functions and generator expressions in the context of systems
programming.  This topic loosely includes files, file systems, text
parsing, network programming, and programming with threads.

`Presentation Slides (PDF) <http://www.dabeaz.com/generators/Generators.pdf>`_  Also available at
https://speakerdeck.com/dabeaz/generator-tricks-for-systems-programmers-version-3-dot-0

Come to Chicago and take a `Course <https://www.dabeaz.com/courses.html>`_. 

Code Samples
------------

The ``examples`` directory contains various code samples and data files
used for the tutorial.  The presentation slides also specify a filename.
This tutorial assumes the use of Python 3.4 or newer.

All of the example programs should be executed within the ``examples``
directory.   Certain programs might require additional support programs
to be running.  This is indicated in the description below.

Part 2 : Processing Data Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `nongenlog.py <examples/nongenlog.py>`_.  Calculate the number of bytes transferred in an Apache server log using a simple for-loop.  Does not use generators.

* `genlog.py <examples/genlog.py>`_. Calculate the number of bytes transferred in an Apache server log using a series of generator expressions.

* `makebig.py <examples/makebig.py>`_. Make a large access-log file for performance testing.  This will create a file "big-access-log".  For the numbers used in the presentation, I used ``python makebig.py 2000``.

Part 3 : Fun with Files and Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `genfind.py <examples/genfind.py>`_. An example of using ``pathlib`` and the ``rglob()`` method to yield filenames matching a given filename pattern.

* `genopen.py <examples/genopen.py>`_.  A generator function that yields filenames matching a given filename pattern.

* `gencat.py <examples/gencat.py>`_.  A generator function that concatenates a sequence of generators into a single sequence.

* `gengrep.py <examples/gengrep.py>`_.  A generator that greps a series of lines for those that match a regex pattern.


Part 4 : Parsing and Processing Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `bytesgen.py <examples/bytesgen.py>`_.  Example that finds out how many bytes were transferred for a specific file in a whole directory of log files.

* `retuple.py <examples/retuple.py>`_.  Parse a sequence of lines into a sequence of tuples using regular expressions.

* `redict.py <examples/redict.py>`_.  Parse a sequence of lines into a sequence of dictionaries with named fields.

* `fieldmap.py <examples/fieldmap.py>`_.  Remap fields in a sequence of dictionaries.

* `linesdir.py <examples/linesdir.py>`_.   Generate lines from files in a directory.

* `apachelog.py <examples/apachelog.py>`_.  Parse an Apache log file.

* `query404.py <examples/query404.py>`_.  Find the set of all documents that are broken (404).

* `largefiles.py <examples/largefiles.py>`_.  Find all requests that transferred over a megabyte.

* `largest.py <examples/largest.py>`_.  Find the largest document.

* `hosts.py <examples/hosts.py>`_.  Find unique host IP addresses.

* `downloads.py <examples/downloads.py>`_.  Find number of downloads of a specific file.

* `robots.py <examples/robots.py>`_.  Find out who has been hitting ``robots.txt``.

Part 5 : Processing Infinite Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `follow.py <examples/follow.py>`_.  Follow a log-file in real-time like ``tail -f`` in Unix.  To run this program, you need to have a log-file to work with.  Run the program `runservers.py <examples/runservers.py>`_ to start a simulated web-server.  This will write a series of log lines for you to follow.

* `realtime404.py <examples/realtime404.py>`_.  Print all 404 requests as they happen in real-time on a log file.

Part 6 : Feeding the Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `genreceive.py <examples/genreceive.py>`_.  Generate clients that connect to a TCP socket.

* `genmessages.py <examples/genmessages.py>`_.  Generate UDP messages.

Part 7 : Extending the pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `genpickle.py <examples/genpickle.py>`_.  Turn sequences of objects into a sequence of pickles.

* `sendto.py <examples/sendto.py>`_.  Send a sequence of items to a remote machine via a socket.  Uses genpickle above.

* `receivefrom.py <examples/receivefrom.py>`_  Receive a sequence of items from a socket.  Uses genpickle above.

* `genqueue.py <examples/genqueue.py>`_.  Consume items on a queue.

Part 8 : Advanced Data Routing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `genmulti.py <examples/genmulti.py>`_.  Generate items from more than one generator at once (multiplexing).

* `broadcast.py <examples/broadcast.py>`_  Broadcast a sequence of items to a collection of consumers.

* `netsend.py <examples/netsend.py>`_.  Send items to another host on the network.  Requires a receiver (use receivefrom.py above).

* `thrsend.py <examples/thrsend.py>`_.  Send items to multiple consumer threads.

Part 9 : Various Programming Tricks (And Debugging)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `gentrace.py <examples/gentrace.py>`_.  Example of debugging a generator component.

* `storelast.py <examples/storelast.py>`_.  Store the last value of a generator (for access later in the processing pipeline)

* `genshutdown.py <examples/genshutdown.py>`_.  Simple example of shutting down a generator.

* `shutdownevt.py <examples/shutdownevt.py>`_.  Shutting down a generator with an event.

Part 10: Parsing and Printing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No sample programs.

Part 11 : Co-routines
~~~~~~~~~~~~~~~~~~~~~

* `recvcount.py <examples/recvcount.py>`_.  A co-routine example.

* `consumer.py <examples/consumer.py>`_.  Co-routine example with a consumer decorator.

* `logcoroutine.py <examples/logcoroutine.py>`_.  Processing log files with co-routines.

Bug Reports
-----------

Bug reports and pull requests to the sample code are welcome. Comments
to dave@dabeaz.com.



