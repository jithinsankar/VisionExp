import numpy as np
import cv2
import base64

stringData64=''

f = open("text.txt",'r')
for i in range (1,1000):
	for line in f:
		stringData64+=line
	f.seek(0,0)
	stringData=base64.decodestring(stringData64) 
	data = np.fromstring(stringData, dtype='uint8')
	frame=cv2.imdecode(data,1)
	cv2.imshow('SERVER',frame)
	stringData=''
	stringData64=''
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()