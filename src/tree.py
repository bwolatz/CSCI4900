#!/usr/bin/env python
import subprocess
import re
import tempfile
import shutil
import os
import treelib

class tree: 
	def __init__(self):
		self.tree = treelib.Tree()
		self.dependencies = {}
		self.relationships = []

	def createTree:
		mvncmd = "mvn -q dependency:tree -Doutput="+os.getcwd()+"/tree/tree.txt -DoutputType=tgf"
		subprocess.call(mvncmd,shell=True)
		txt = open(tree.txt)
		print txt.read()
			 
		
