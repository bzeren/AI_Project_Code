import SOM 
import numpy as np
import random
import matplotlib as mpl

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

som1 = SOM.SOM(20,20,8,0.5,2)

# print som1.matrix
# print som1.get_value(0,0)

from PIL import Image

##Load image
im = Image.open("landscape.jpg")
# im.show()
imgplot = plt.imshow(im)
plt.show()

width, height = im.size
# print im.size
r, g, b = im.split()


px = im.load()


for i in range(1000): #number of iterations

	random_x = random.randint(0,width-1)
	random_y = random.randint(0,height-1)

	I = np.asarray(px[random_x,random_y])/255.0
	
	(xc,yc) = som1.find_closest(I)

	som1.update_value(xc,yc,som1.alpha,som1.R,I)


somout = np.multiply(som1.matrix,255).astype(int)
imgplot2=plt.imshow(som1.matrix,interpolation="nearest")
plt.show()

