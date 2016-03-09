#!/usr/bin/env python
"""Imports"""
import subprocess
import glob
import os

currentdir = "/home/nikhit/Results/dependencies"

mvncommand = "mvn -q dependency:copy-dependencies -DcopyPom=true -DoutputDirectory="+currentdir

subprocess.call(mvncommand, shell=True)

os.chdir(currentdir)
for jar in glob.glob('*.jar'):
	subprocess.call('dosocs2 oneshot '+jar, shell=True)


