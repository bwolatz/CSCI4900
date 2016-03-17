#!/usr/bin/env python
import subprocess
import os
import re
import shutil

class Dependency:
	"""Dependency Object"""

	def __init__(self):
		os.makedirs(os.getcwd()+"/jar")
		self.tempdir = os.getcwd()+"/jar"

	def copyPom(self, pathtopom):
		shutil.copy(pathtopom, self.tempdir)
		os.chdir(self.tempdir)

	def getDependenciesandScan(self):
		mvncmd = "mvn -q dependency:copy-dependencies -DcopyPom=true -DoutputDirectory="+self.tempdir
		mvncmd1 = "mvn -q dependency:tree -Doutput=" + self.tempdir + "/tree.txt -DoutputType=text" 
		subprocess.call(mvncmd, shell=True)
		subprocess.call(mvncmd1, shell=True)
		p = re.compile('^[A-z]+$')
		print("Starting to scan dependencies.")
	        count = 0
	        dep1Jars = []
	        dep2Jars = []
	        dep3Jars = []
	        depfile = open('tree.txt', 'r+')
	        for line in depfile:
	                """ skip first line """
	                if count == 0:
	                        count += 1
	                elif len(line) > 9:
	                        if p.match(line[3]) and line[3] != '\\':
	                                dep1Jars.append(line[3:])
	                        elif p.match(line[6]) and line[6] != '\\':
	                                dep2Jars.append(line[6:])
				elif p.match(line[9]) and line[9] != '\\':
        	                        dep3Jars.append(line[9:])
		strin = ""
        	for jar1 in dep1Jars:
                	jar1.rstrip()
                	strin = jar1.split(':')
                	jar1 = strin[1] + "-" + strin[3] + ".jar"
                	output = subprocess.Popen(['dosocs2', 'scan', jar1], stdout=subprocess.PIPE)
                	out = output.stdout.read()
                	out.rstrip()

		for jar2 in dep2Jars:
	                jar2.rstrip()
	                strin = jar2.split(':')
	                jar2 = strin[1] + "-" + strin[3] + ".jar"
	                output = subprocess.Popen(['dosocs2', 'scan', jar2], stdout=subprocess.PIPE)
	                out = output.stdout.read()
	                out.rstrip()
	
	        for jar3 in dep3Jars:
	                jar3.rstrip()
	                strin = jar3.split(':')
	                jar3 = strin[1] + "-" + strin[3] + ".jar"
	                output = subprocess.Popen(['dosocs2', 'scan', jar3], stdout=subprocess.PIPE)
	                out = output.stdout.read()
	                out.rstrip()

