import numpy as np

## Reading the data from csv file as arrays
data = np.genfromtxt ('data.csv', delimiter = ',')
print("\n Printing the data from the csv file.\n")

default_angles=np.array([225, 270, 315,0,45,90,135,180])
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
		print w
		w=round(w)

		if(i<7):
			SOM_Feature[(global_angle/45)%8]= row[i]*w + row[i+1]*(1-w)
		else:
			SOM_Feature[(global_angle/45)%8]=row[i]*w + row[0]*(1-w)
			
	print SOM_Feature