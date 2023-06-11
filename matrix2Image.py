from PIL import Image
import numpy as np
w, h = 1024, 1024
data = np.zeros((h, w, 3), dtype=np.uint8)
#data[0:256, 0:256] = [255, 0, 0] # red patch in upper left.
for x in range(w):
	a=0
	for y in range(h):
		a=(x+y)%4
		if a==0:
			data[x,y] = [255, 0, 0] # red patch in upper left.

		else:
			data[x,y] = [255, 255, 255] # red patch in upper left.

for x in range(256,256+ w//2):
	a=0
	for y in range(256,256+ h//2):
		a=(x+y)%2
		if a==0:
			data[x,y] = [255, 0, 0] # red patch in upper left.

		else:
			data[x,y] = [255, 255, 255] # red patch in upper left.



	
img = Image.fromarray(data, 'RGB')
img.save('k_b.png')
img.show()
