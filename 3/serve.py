 # -*- coding: utf-8 -*- 
from flask import Flask
import json


app = Flask(__name__)
@app.route('/node')
def helloHandler():
	stringData=''
	f = open("text.txt",'r')
	for line in f:
		stringData+=line
	f.seek(0,0)
	return stringData
app.run(host='0.0.0.0', port= 8090)

#http://192.168.43.112:8090/helloesp
