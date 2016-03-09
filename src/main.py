#!/usr/bin/env python
"""Imports"""
import subprocess
import glob
import os

currentdir = "/usr/share/fossology/nomos/agent/jars"
pomdir = "/usr/share/fossology/nomos/agent/"
mvncommand = "mvn -q dependency:copy-dependencies -DcopyPom=true -DoutputDirectory="+currentdir
mvncommand2 = "mvn dependency:tree -Doutput=" + pomdir + "/tree.txt -DoutputType=text"

subprocess.call(mvncommand, shell=True)

os.chdir(pomdir)
subprocess.call(mvncommand2, shell=True)

os.chdir(currentdir)
for jar in glob.glob('*.jar'):
    subprocess.call('dosocs2 oneshot '+jar, shell=True)
