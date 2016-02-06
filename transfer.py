import subprocess;
import re;
import MySQLdb;
import sys;

#fname = re.compile("[a-zA-z]+\.[a-zA-z]+");
#lname = re.compile("\S+$");
pos = 0;
count = 0;
results = [];
for arg in sys.argv:
	if(count > 0):
		results[pos] = subprocess.check_output(["/usr/share/fossology/nomos/agent/nomos","-d","/home/nikhit/%s"%(arg,)]);
		pos+=1;
	count += 1;
everything = [];	
for match in results:
	everything.insert(re.split("\s+",match));
#for match in everything:
#	print "Everything: ",match;
count = 1;
pos = 0;
filename = [];
license = [];
for match in everything:
	if(count == 2):
		filename.insert(pos,match)
	elif(count == 5):
		license.insert(pos,match)
		count = 0
		pos += 1
	count += 1;

print len(filename);
print len(license);
for match in filename:
	print "FileName: ",match;
for match in license:
	print "License: ",match;


#filename = fname.finditer(results);
#licensename = lname.finditer(results);
#for match in filename:
#	print "File Name: ",match.group();
#for match in licensename:
#	print "License: ",match.group();
pos = 0;
connect = MySQLdb.connect(host='localhost',
                          user='root',
                          passwd='Nikhit',
                          db='Details');
cur = connect.cursor();
for match in filename:
	cur.execute("""INSERT INTO License (filename,license) VALUES (%s,%s)""",(match,license[pos]));
	pos += 1;
connect.commit();
connect.close();	
