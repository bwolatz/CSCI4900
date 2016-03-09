#!/usr/bin/env python
"""Imports"""
from subprocess import call
import glob
import os

currentdir = "/home/nikhit/Results/dependencies"

mvncommand = "mvn -q dependency:copy-dependencies -DcopyPom=true -DoutputDirectory="+currentdir

call(mvncommand, shell=True)

os.chdir(currentdir)
for jar in glob.glob('*.jar'):
	call('dosocs2 oneshot '+jar, shell=True)


