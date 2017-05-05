

import requests
import sys

if len(sys.argv) != 2:
	print ("USAGE: %s URL" %(sys.argv[0]))
	sys.exit(0)

url = str(sys.argv[1])


req = requests.get(url)

for cookie in req.cookies:
	print ("Name:", cookie.name)
	print ("Value:", cookie.value)

	if not cookie.secure:
		cookie.secure = '\x1b[31mFalse\x1b[39;49m'

	print ('Secure: ', cookie.secure)


	if 'httponly' in cookie._rest.keys():
		cookie.httponly = 'True'
	else:
		cookie.httponly = '\x1b[31mFalse\x1b[39;49m'

	print ("HTTP ONLY: ", cookie.httponly)


	if cookie.domain_initial_dot:
		#\x1b change de color of the terminal
		cookie.domain_initial_dot  = '\x1b[31mTrue\x1b[39;49m'
		#If the domain attribute of the cookie starts with a dot, it indicates the cookie is used...
		#across all subdomains and therefore possibly visible beyond the intended scope.
	print ('Loosly defined domain: ', cookie.domain_initial_dot, '\n')
