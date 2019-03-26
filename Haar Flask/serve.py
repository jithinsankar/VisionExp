 # -*- coding: utf-8 -*- 
from flask import Flask
import json
import numpy as np
import cv2
import base64

cap = cv2.VideoCapture(0)
app = Flask(__name__)
@app.route('/payload')
def helloHandler():
	ret, frame = cap.read()
	encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
	result, imgencode = cv2.imencode('.jpg', frame, encode_param)
	data = np.array(imgencode)
	stringData = data.tostring()
	stringData64=base64.encodestring(stringData)
	return stringData64
app.run(host='0.0.0.0', port= 8090)

#http://192.168.43.112:8090/payload
