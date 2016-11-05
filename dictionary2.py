import requests
import json


wordFrom = "http://challenge.code2040.org/api/haystack"
myToken = {'token':'b02a6c9eeaf28fac7d94e2cec7e89680'}


def connection(url,data):
	request = requests.post(wordFrom, data = myToken)
	readDictionary = json.loads(request.content)
	return readDictionary


def search(needle, haystack):
	return haystack.index(needle)


dictionary =  connection(wordFrom,myToken)

needle=dictionary['needle']
haystack= dictionary['haystack']

exists= search(needle,haystack)

validate = "http://challenge.code2040.org/api/haystack/validate"



send= requests.post(validate,json={'token':'b02a6c9eeaf28fac7d94e2cec7e89680','needle': exists})
