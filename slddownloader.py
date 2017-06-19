#!/usr/bin/python
import urllib
for x in range(1,34):
	urllib.urlretrieve("https://image.slidesharecdn.com/xxx/95/xx-"+str(x)+"-xxx.jpg?cb=xxxxxxxx",str(x)+".jpg")
#document.querySelector('.slide_image').src take link in your browser's console.
