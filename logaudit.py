#!/usr/bin/python3
#me@danielpeluso.com

import sys
import os
import re

os.chdir('/var/log') #change directory to location of file

document = open("auth.log", "r") #open file in read mode 

for line in document:
   if re.match("(.*)(F|f)ailed(.*)", line): #regex to find lines with failure
      print (line)
   else:
      print('nothing here to see!') #message if no hits return
