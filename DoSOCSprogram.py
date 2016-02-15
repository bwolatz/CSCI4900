#!/usr/bin/env python
import subprocess;
import re;
import sys;

#Declaring the variables for the program
count = 0;
pos = 0;
results = [];

#loop to check and get all the lines of output from nomos for all the files. 
for arg in sys.argv:
        if(count > 0):
                results.insert(pos,subprocess.check_output(["dosocs2","oneshot","/home/nikhit/%s"%(arg,)]));
                pos += 1;
        count += 1;

#Just printing all the output that is stored.
for match in results:
        print match;

