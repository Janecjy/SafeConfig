def checkSecurePass(password):
	hasLower, hasHigher, hasDigit = False, False, False
	for letter in password:
		hasLower = hasLower or letter.islower()
		hasHigher = hasHigher or letter.isupper()
		hasDigit = hasDigit or letter.isdigit()
	return hasLower and hasHigher and hasDigit

def dealPass(password):
	if checkSecurePass(password) == True:
		return "******"
	else:
		return "not secure password"

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
