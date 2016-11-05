
import urllib

myToken = {'token':'b02a6c9eeaf28fac7d94e2cec7e89680'}
wordFrom = "http://challenge.code2040.org/api/reverse"


def connection(url, data):
	urlConnect = urllib.urlopen(url, urllib.urlencode(data))
	word = urlConnect.read()
	return word

string = connection(wordFrom,myToken)
print string


url = "http://challenge.code2040.org/api/reverse/validate"
reverse = string[::-1]
print reverse


data = {'token':'b02a6c9eeaf28fac7d94e2cec7e89680',"string": reverse}
response = connection(url, data)

print response


