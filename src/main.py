#!/usr/bin/env python
"""Imports"""
import subprocess
import glob
import os
import re

__version__ = '0.0.1'

def main():
	pomdir = os.getcwd()
	jardir = pomdir + "/jars"
	treedir = pomdir + "/tree"
	mvncommand = "mvn -q dependency:copy-dependencies -DcopyPom=true -DoutputDirectory="+jardir
	mvncommand2 = "mvn -q dependency:tree -Doutput=" + treedir + "/tree.txt -DoutputType=tgf"

	subprocess.call(mvncommand, shell=True)

	os.chdir(pomdir)
	subprocess.call(mvncommand2, shell=True)

	os.chdir(treedir)
	p = re.compile('^[A-z]+$')
	count = 0
	dep1Jars = []
	dep2Jars = []
	dep3Jars = []
	depfile = open('tree.txt', 'r')
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

	os.chdir(jardir)
	str = ""
	for jar1 in dep1Jars:
    		jar1.rstrip()
    		str = jar1.split(':')
    		jar1 = str[1] + "-" + str[3] + ".jar"
    		subprocess.call('dosocs2 scan '+jar1, shell=True)

	for jar2 in dep2Jars:
    		jar2.rstrip()
    		str = jar2.split(':')
    		jar2 = str[1] + "-" + str[3] + ".jar"
   		subprocess.call('dosocs2 scan '+jar2, shell=True)

	for jar3 in dep3Jars:
    		jar3.rstrip()
    		str = jar3.split(':')
    		jar3 = str[1] + "-" + str[3] + ".jar"
    		subprocess.call('dosocs2 scan '+jar3, shell=True)
