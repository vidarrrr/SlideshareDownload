#!/usr/bin/python
import urllib
import sys
if(len(sys.argv)!=3):
	print("Usage python slddownloader.py link pagecount+1")
	sys.exit(1)
data=sys.argv[1];
data1=data.split('-1-')

for x in range(1,int(sys.argv[2])):
	urllib.urlretrieve(data1[0]+'-'+str(x)+'-'+data1[1],str(x)+".jpg")
#document.querySelector('.slide_image').src take link in your browser's console.
