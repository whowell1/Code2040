import json
import requests



wordFrom = "http://challenge.code2040.org/api/prefix"
myToken = {'token':'b02a6c9eeaf28fac7d94e2cec7e89680'}


def connection(url,data):
	request = requests.post(wordFrom, data = myToken)
	readDictionary = json.loads(request.content)
	return readDictionary

dictionary=connection(wordFrom,myToken)

prefix = dictionary['prefix']
lengthPrefix = len(prefix)
array = dictionary['array']


array = [i for i in array if i[:lengthPrefix] != prefix]
validate = 'http://challenge.code2040.org/api/prefix/validate'

send = requests.post(validate, json = {'token':'b02a6c9eeaf28fac7d94e2cec7e89680', 'array': array})
