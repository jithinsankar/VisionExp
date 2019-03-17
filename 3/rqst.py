import requests
import json
import cv2
import  numpy as np
import base64


while True:
	try:
		r = requests.get('http://192.168.43.112:8090/node')
		stringData64=r.text
		stringData64 += "=" * ((4 - len(stringData64) % 4) % 4)
		stringData=base64.decodestring(stringData64) 
		data = np.fromstring(stringData, dtype='uint8')
		frame=cv2.imdecode(data,1)
		cv2.imshow('SERVER',frame)
	except:
		pass
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
stringData=''
stringData64=''
print r.text
