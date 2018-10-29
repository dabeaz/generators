#!/bin/sh
cd run/foo; python logsim.py &
cd run/bar; sleep(600); python logsim.py &
