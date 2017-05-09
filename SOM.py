import numpy as np

class SOM: 

	def __init__(self, x, y, d, alpha, R):
		self.x = x
		self.y = y
		self.d = d
		self.alpha = alpha
		self.R = R
		self.matrix = np.random.rand(x,y,d)

	def get_value(self,x,y):
		return self.matrix[x][y]

	def distance(self,x,y,I):
		return np.sqrt(np.dot(self.matrix[x][y]-I, self.matrix[x][y]-I))

	def find_closest(self, I):
		value = float("inf")
		x_closest = 0
		y_closest = 0
		for i in range(self.x):
			for j in range(self.y):				
					dot = self.distance(i,j,I)
					if dot < value:
						value = dot
						x_closest = i
						y_closest = j
		return (x_closest,y_closest)


	# def find_neighbors(x,y):
	# 	return np.array([(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)])

	def update_value(self, xc,yc,alpha,R, I):
		"""
		For all nodes (x,y) and their neighbors (according to the neighbor definition)
		"""
		for x in range(self.x):
			for y in range(self.y):
				coef = self.alpha/(np.sqrt((x-xc)**2+(y-yc)**2)+1)
				
				self.matrix[x][y] = ((1-coef) * self.matrix[x][y]) + (coef * I) 
		return self.matrix[x][y]

	def activation(self,array):
		actv_array = []

		for i in range(8):
			actv_val = (array[i]-10) / 10.0
			if actv_val > 0:
				actv_val = 0 
			else:
				actv_val = abs(actv_val)
			actv_array.append(actv_val)
		return np.asarray(actv_array)






		

















