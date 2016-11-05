import json
import requests
import arrow

wordFrom = "http://challenge.code2040.org/api/dating"
myToken = {'token':'b02a6c9eeaf28fac7d94e2cec7e89680'}


def connection(url,data):
	request = requests.post(wordFrom, data = myToken)
	readDictionary = json.loads(request.content)
	return readDictionary




dictionary=connection(wordFrom,myToken)

time = dictionary['datestamp']
interval = dictionary['interval']
utc = arrow.get(time)

timeNow = utc.timestamp
timeNow+= interval

convert = arrow.Arrow.utcfromtimestamp(timeNow).format('YYYY-MM-DDTHH:mm:ss') + 'Z'

validate = 'http://challenge.code2040.org/api/dating/validate'
send = requests.post(validate, json = {'token':'b02a6c9eeaf28fac7d94e2cec7e89680', 'datestamp': convert})