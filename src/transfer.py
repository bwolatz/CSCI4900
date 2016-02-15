#!/usr/bin/env python
import subprocess;
import re;
import MySQLdb;
import sys;

#Declaring the variables for the program
count = 0;
pos = 0;
results = [];

#loop to check and get all the lines of output from nomos for all the files. 
for arg in sys.argv:
	if(count > 0):
		results.insert(pos,subprocess.check_output(["/usr/share/fossology/nomos/agent/nomos","-d","/home/nikhit/%s"%(arg,)]));
		pos += 1;
	count += 1;

#Loops for the program to check all the lines of output and split and store the filename and the license into separate sets of loops
counter = 0;
allinfo = [];
for match in results:
	everything = re.findall('File\s+(\S+)\s+\S+\s+\S+\s+(\S+)\s+',match);
	for x in everything: 
		allinfo.insert(counter,x);
print allinfo;
#Storing the correct filename and license information into a MYSQL database.
connect = MySQLdb.connect(host='localhost',
                          user='root',
                          passwd='Nikhit',
                          db='Details');
cur = connect.cursor();
for match in allinfo:
	cur.execute("""INSERT INTO license (filename,license) VALUES (%s,%s)""",(match[0],match[1]));
connect.commit();
connect.close();
