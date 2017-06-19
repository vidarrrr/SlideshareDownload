#!/usr/bin/python
import urllib
for x in range(1,34):
	urllib.urlretrieve("https://image.slidesharecdn.com/istsecsunum-170505210512/95/stsec17-kresel-siber-sula-mcadele-ve-trend-saptrma-teorisi-"+str(x)+"-638.jpg?cb=1494018394",str(x)+".jpg")
#document.querySelector('.slide_image').src take link in your browser's console.
