def checkSecurePass(password):
	for letter in password:
		hasLower = letter.islower()
		hasHigher = letter.isupper()
		hasDigit = letter.isdigit()
	return hasLower and hasHigher and hasDigit

def dealPass(password):
	content = ""
	if checkSecurePass(password) == True:
		for x in range(len(password)):
			content += "*"
	else:
		content = "not secure password"
	return content

def dealRename(command):
	return command.split()[0] + " " + "******"

def init():
	app_dict = {}
	wordpressDefault = []
	wordpressSensitive = ['AUTH_KEY', 'SECURE_AUTH_KEY', 'LOGGED_IN_KEY', 'NONCE_KEY', 'AUTH_SALT', 'SECURE_AUTH_SALT',
						  'LOGGED_IN_SALT',
						  'NONCE_SALT', 'DB_PASSWORD']
	wordpressDealingFunc = [dealPass, dealRename]
	app_dict["default"] = wordpressDefault
	app_dict["sensitive"] = wordpressSensitive
	app_dict["dealingFunc"] = wordpressDealingFunc
	return app_dict
