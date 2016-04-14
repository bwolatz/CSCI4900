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
                mvncmd2 = "mvn -q dependency:tree -Doutput=" + self.tempdir + "/tree.txt -DoutputType=text"
                lastl2 = "";
                lastl1 = "";
                subprocess.call(mvncmd, shell=True)
                subprocess.call(mvncmd2, shell=True)
                p = re.compile('^[A-z]+$')
                print("Starting to scan dependencies.")
                count = 0
                dep1Jars = []
                dep1JarI = []
                dep2Jars = []
                dep2JarI = []
                dep2JarsP = []
                dep3Jars = []
                dep3JarI = []
                dep3JarsP = []
                depfile = open('tree.txt', 'r+')
                for line in depfile:
                        """ skip first line """
                        if count == 0:
                                count += 1
                        elif len(line) > 9:
                                if p.match(line[3]) and line[3] != '\\':
                                        dep1Jars.append(line[3:])
                                        lastl1 = line[3:]
                                elif p.match(line[6]) and line[6] != '\\':
                                        dep2Jars.append(line[6:])
                                        dep2JarsP.append(lastl1)
                                        lastl2 = line[6:]
                                elif p.match(line[9]) and line[9] != '\\':
                                        dep3Jars.append(line[9:])
                                        dep3JarsP.append(lastl2)
                count = 0
                for l2jar in dep2Jars:
                        count += 1
                count = 0
                for l3jar in dep3Jars:
                        count += 1
                if os.path.exists(self.tempdir):
                        os.chdir(self.tempdir)
                        pkgFile = open("pkg.txt", "w")
                        token = ""
                        output = ""
                        line = ""
                        docinfo = ""
                        docid = ""
                print("Scanning level-1 dependencies")
                for jar1 in dep1Jars:
                        jar1.rstrip()
                        token = jar1.split(':')
                        jar1 = token[1]+"-"+token[3]+".jar"
                        output = subprocess.Popen('dosocs2 scan '+jar1, stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, shell=True)
                        line = output.stdout.readline().rstrip()
                        match = re.match(r".*package_id:\s?(\d+)",line)
                        if(match):
				print 'Generating level-1 documents'
                                docinfo = subprocess.Popen('dosocs2 generate '+match.group(1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                                #docid = docinfo.stdout.readline().rstrip()
                                #print docid
                                #docmatch = re.match(r".*document_id:\s?(\d+)",docid)
                                #print 'Document Id: '+docmatch.group(1)
                                #print subprocess.check_output(['dosocs2','print',docmatch.group(1)])
                        	dep1JarI.append(match.group(1))
                        
                print("Scanning level-2 dependencies")
		for jar2 in dep2Jars:
                        jar2.rstrip()
                        token = jar2.split(':')
                        jar2 = token[1] + "-" + token[3] + ".jar"
                        output = subprocess.Popen('dosocs2 scan '+ jar2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                        line =  output.stdout.readline().rstrip()
                        match = re.match(r".*package_id:\s?(\d+)",line)
                        if(match):
				print 'Generating level-2 documents'
                                docinfo = subprocess.Popen('dosocs2 generate '+match.group(1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                                #docid = docinfo.stdout.readline().rstrip()
                                #print docid
                                #docmatch = re.match(r".*document_id:\s?(\d+)",docid)
                                #print 'Document Id: '+docmatch.group(1)
                                #print subprocess.check_output(['dosocs2','print',docmatch.group(1)])
                        	dep2JarI.append(match.group(1))
                        
                print("Scanning level-3 dependencies")
                for jar3 in dep3Jars:
                        jar3.rstrip()
                        token = jar3.split(':')
                        jar3 = token[1] + "-" + token[3] + ".jar"
                        output = subprocess.Popen('dosocs2 scan '+jar3,stdout = subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                        line = output.stdout.readline().rstrip()
                        match = re.match(r".*package_id:\s?(\d+)",line)
                        if(match):
				print 'Generating level-3 documents'
                                docinfo = subprocess.Popen('dosocs2 generate '+match.group(1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                                #docid = docinfo.stdout.readline().rstrip()
                                #print docid
                                #docmatch = re.match(r".*document_id:\s?(\d+)",docid)
                                #print 'Document Id: '+docmatch.group(1)
                                #print subprocess.check_output(['dosocs2','print',docmatch.group(1)])
                        	dep3JarI.append(match.group(1))
                        
                count = 0
                for l2jar in dep2Jars:
                        otherI = 0
			if(count < len(dep2JarI)):
                        	thisI = dep2Jars[count]
                        #print l2jar + "\' is a dependent of \'" + dep2JarsP[count] + "\'"
                        count2 = 0
                        for parentJar in dep1Jars:
                                if dep2JarsP[count] == parentJar:
                                        if(count < len(dep1JarI)):
						otherI = dep1Jars[count2]
                                        break
                                count2 += 1
                        count += 1
                        if otherI != 0: 
                        	subprocess.call(['dosocs2','relation',otherI,thisI])
                        
                        
                count = 0
                for l3jar in dep3Jars:
                        otherI = 0
                        if(count < len(dep3JarI)):
				thisI = dep3Jars[count]
                        #print l2jar + "\' is a dependent of \'" + dep2JarsP[count] + "\'"
                        count2 = 0
                        for parentJar in dep2Jars:
                                if dep3JarsP[count] == parentJar:
                                        if(count < len(dep2JarI)):
						otherI = dep2Jars[count2]
                                        break
                                count2 += 1
                        count += 1
                        if otherI != 0:
                        	subprocess.call(['dosocs2','relation',otherI,thisI])
