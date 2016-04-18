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
    
    def getDependencies(self):
        mvncmd = "mvn -q dependency:copy-dependencies -DcopyPom=true -DoutputDirectory="+self.tempdir
        subprocess.call(mvncmd, shell=True)

    def getTree(self):
        mvncmd2 = "mvn -q dependency:tree -Doutput=" + self.tempdir + "/tree.txt -DoutputType=text"
        subprocess.call(mvncmd2, shell=True)

    def scanTreeForLevels(self):
        lastl2 = "";
        lastl1 = "";
        p = re.compile('^[A-z]+$')
        #print("Starting to scan dependencies.")
        count = 0
        self.dep1Jars = []
        self.dep1JarI = []
        self.dep2Jars = []
        self.dep2JarI = []
        self.dep2JarsP = []
        self.dep3Jars = []
        self.dep3JarI = []
        self.dep3JarsP = []
        depfile = open('tree.txt', 'r+')
        for line in depfile:
            """ skip first line """
            if count == 0:
                count += 1
            elif len(line) > 9:
                if p.match(line[3]) and line[3] != '\\':
                    toAdd = line[3:]
                    toAdd.rstrip()
                    self.dep1Jars.append(toAdd)
                    lastl1 = toAdd
                elif p.match(line[6]) and line[6] != '\\':
                    toAdd = line[6:]
                    toAdd.rstrip()
                    self.dep2Jars.append(toAdd)
                    self.dep2JarsP.append(lastl1)
                    lastl2 = toAdd
                elif p.match(line[9]) and line[9] != '\\':
                    toAdd = line[9:]
                    toAdd.rstrip()
                    self.dep3Jars.append(toAdd)
                    self.dep3JarsP.append(lastl2)
        print self.dep1Jars

    def scanDependenciesByLevel(self):  
        if os.path.exists(self.tempdir):
            os.chdir(self.tempdir)
            pkgFile = open("pkg.txt", "w")
            token = ""
            output = ""
            line = ""
            docinfo = ""
            docid = ""
        #print("Scanning level-1 dependencies")
        for jar1 in self.dep1Jars:
            jar1.rstrip()
            token = jar1.split(':')
            jar1 = token[1]+"-"+token[3]+".jar"
            output = subprocess.Popen('dosocs2 scan '+jar1, stdout=subprocess.PIPE ,stderr=subprocess.STDOUT, shell=True)
            line = output.stdout.readline().rstrip()
            match = re.match(r".*package_id:\s?(\d+)",line)
            if(match):
                #print 'Generating level-1 documents'
                docinfo = subprocess.Popen('dosocs2 generate '+match.group(1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                #docid = docinfo.stdout.readline().rstrip()
                #print docid
                #docmatch = re.match(r".*document_id:\s?(\d+)",docid)
                #print 'Document Id: '+docmatch.group(1)
                #print subprocess.check_output(['dosocs2','print',docmatch.group(1)])
                self.dep1JarI.append(match.group(1))
                print self.dep1JarI

        #print("Scanning level-2 dependencies")
        for jar2 in self.dep2Jars:
            jar2.rstrip()
            token = jar2.split(':')
            jar2 = token[1] + "-" + token[3] + ".jar"
            output = subprocess.Popen('dosocs2 scan '+ jar2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            line =  output.stdout.readline().rstrip()
            match = re.match(r".*package_id:\s?(\d+)",line)
            if(match):
                #print 'Generating level-2 documents'
                docinfo = subprocess.Popen('dosocs2 generate '+match.group(1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                #docid = docinfo.stdout.readline().rstrip()
                #print docid
                #docmatch = re.match(r".*document_id:\s?(\d+)",docid)
                #print 'Document Id: '+docmatch.group(1)
                #print subprocess.check_output(['dosocs2','print',docmatch.group(1)])
                self.dep2JarI.append(match.group(1))
                print self.dep2JarI    
                
        #print("Scanning level-3 dependencies")
        for jar3 in self.dep3Jars:
            jar3.rstrip()
            token = jar3.split(':')
            jar3 = token[1] + "-" + token[3] + ".jar"
            output = subprocess.Popen('dosocs2 scan '+jar3,stdout = subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            line = output.stdout.readline().rstrip()
            match = re.match(r".*package_id:\s?(\d+)",line)
            if(match):
                #print 'Generating level-3 documents'
                docinfo = subprocess.Popen('dosocs2 generate '+match.group(1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                #docid = docinfo.stdout.readline().rstrip()
                #print docid
                #docmatch = re.match(r".*document_id:\s?(\d+)",docid)
                #print 'Document Id: '+docmatch.group(1)
                #print subprocess.check_output(['dosocs2','print',docmatch.group(1)])
                self.dep3JarI.append(match.group(1))
                print self.dep3JarI
    
    def createRelationshipDoc(self):
        #print("creating relationship doc")
        count = 0
        for l2jar in self.dep2Jars:
            otherI = 0
            if(count < len(self.dep2JarI)):
                thisI = self.dep2Jars[count]
                #print l2jar + "\' is a dependent of \'" + dep2JarsP[count] + "\'"
            count2 = 0
            for parentJar in self.dep1Jars:
                if self.dep2JarsP[count2] == parentJar:
                    if(count2 < len(self.dep1JarI)):
                        otherI = self.dep1JarI[count2]
                    break
                count2 += 1
            count += 1
            if otherI != 0: 
                subprocess.call(['dosocs2','relation',otherI,thisI])
                subprocess.call(['dosocs2','print','otherI'])
                print " has a dependent "
                subprocess.call(['dosocs2','print','thisI'])
                        
        count = 0
        for l3jar in self.dep3Jars:
            otherI = 0
            if(count < len(self.dep3JarI)):
                thisI = self.dep3Jars[count]
                #print l2jar + "\' is a dependent of \'" + dep2JarsP[count] + "\'"
                count2 = 0
                for parentJar in self.dep2Jars:
                    if self.dep3JarsP[count] == parentJar:
                        if(count2 < len(self.dep2JarI)):
                            otherI = self.dep2JarI[count2]
                        break
                    count2 += 1
                count += 1
                if otherI != 0:
                    subprocess.call(['dosocs2','relation',otherI,thisI])
                    subprocess.call(['dosocs2','print','otherI'])
                    print " has a dependent "
                    subprocess.call(['dosocs2','print','thisI'])
                
