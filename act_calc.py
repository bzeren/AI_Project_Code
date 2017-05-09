import numpy as np

def activation(array):
		actv_array = []

		for i in range(8):
			actv_val = (array[i]-10) / 10.0
			if actv_val > 0:
				actv_val = 0 
			else:
				actv_val = abs(actv_val)
			actv_array.append(actv_val)
		return np.asarray(actv_array)

array = [7.37780607, 10.39298434, 1.440149917, 2.028714067, 10.62233386, 5.728803966, 4.034970865, 
5.683991748]

print activation(array)

