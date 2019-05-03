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
	redisDefault = ["bind", "protected-mode", "port", "unixsocketperm", "requirepass", "rename-command"]
	redisSensitive = ["requirepass", "rename-command"]
	redisDealingFunc = [dealPass, dealRename]
	app_dict["default"] = redisDefault
	app_dict["sensitive"] = redisSensitive
	app_dict["dealingFunc"] = redisDealingFunc
	return app_dict
