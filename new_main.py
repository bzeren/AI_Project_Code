import SOM 
import numpy as np
import random
import csv 

som1 = SOM.SOM(20,20,8,0.5,2)

## Reading the data from csv file as arrays
data = np.genfromtxt ('data_room_square.csv', delimiter = ',')
print("\n Printing the data from the csv file.\n")

data=np.random.permutation(data)

default_angles=np.array([225, 270, 315,0,45,90,135,180])
name=0


for row in data:
	val=0;
	SOM_Feature=np.zeros(8)
	if(row[11]<0):
		val=180 + 180*((row[11]+np.pi))/(np.pi)
	else:
		val=360*(row[11]/(2*np.pi))

	final_angles=(default_angles+val)%360

	for i in range(8):
		sensor=row[i]
		robot_angle=final_angles[i]
		global_angle= (int(robot_angle/45)+1)*45

		if abs(global_angle-robot_angle)<180:
			w= 1-((global_angle - robot_angle)/45.0)
		else:
			w=1-((360-(global_angle-robot_angle))/45.0)
		w=round(w)

		if(i<7):
			SOM_Feature[(global_angle/45)%8]= row[i]*w + row[i+1]*(1-w)
		else:
			SOM_Feature[(global_angle/45)%8]=row[i]*w + row[0]*(1-w)
	
	if(random.random()<0.5):

		I = som1.activation(SOM_Feature)
		
		(xc,yc) = som1.find_closest(I)

		som1.update_value(xc,yc,som1.alpha,som1.R,I)		
		name=name+1
		f = open('SOM_room_square'+str(name)+'.csv', 'w')

		for i in range(20):
			for j in range (20):
				line = som1.matrix[i][j]
				for t in range(8):
					if(t<7):
						f.write(str(line[t]))
						f.write(",")
					else:
						f.write(str(line[t]))
						f.write("\n")





