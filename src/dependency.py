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
		if os.path.exists(self.tempdir):
	                os.chdir(self.tempdir)
        		pkgFile = open("pkg.txt", "w")
			token = ""
			output = ""
        	for jar1 in dep1Jars:
			print("Scanning level-1 dependencies")
                        jar1.rstrip()
                        token = jar1.split(':')
                        jar1 = token[1]+"-"+token[3]+".jar"
			
<<<<<<< HEAD
			output = subprocess.Popen('dosocs2 scan '+jar1, stdout=subprocess.PIPE , shell=True)
                	print'printing thing'
                	print('Level - 1: '+output.stdout.readline().rstrip())
=======
			output = subprocess.check_output(['dosocs2', 'oneshot',jar1])
                	print'printing thing'
                	print('Level - 1: '+str(output))
>>>>>>> 82160ec2a07ef9caa9aa8f59818dd1ca00af4631
                	print'end'

                for jar2 in dep2Jars:
                        print("Scanning level-2 dependencies")
                        jar2.rstrip()
                        token = jar2.split(':')
                        jar2 = token[1] + "-" + token[3] + ".jar"
<<<<<<< HEAD
                        output = subprocess.Popen('dosocs2 scan '+ jar2, stdout=subprocess.PIPE, shell=True)
                	print 'printing thing'
                	print output.stdout.readline().rstrip()
=======
                        output = subprocess.check_output(['dosocs2', 'oneshot', jar2])
                	print 'printing thing'
                	print output
>>>>>>> 82160ec2a07ef9caa9aa8f59818dd1ca00af4631
                	print 'end'

                for jar3 in dep3Jars:
                        print("Scanning level-3 dependencies")
                        jar3.rstrip()
                        token = jar3.split(':')
                        jar3 = token[1] + "-" + token[3] + ".jar"
<<<<<<< HEAD
                	output = subprocess.Popen('dosocs2 scan '+jar3,stdout = subprocess.PIPE, shell=True)
                	print 'printing thing'
                	print output.stdout.readline().rstrip()
=======
                	output = subprocess.check_output(['dosocs2', 'oneshot', jar3])
                	print 'printing thing'
                	print output
>>>>>>> 82160ec2a07ef9caa9aa8f59818dd1ca00af4631
                	print 'end'
