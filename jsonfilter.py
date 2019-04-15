import sys
import json

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

def main():
	app_type = ["redis", "mongodb", "nginx", "spark", "tomcat", "wordpress", "joomla"]

	redisDefault = ["bind", "protected-mode", "port", "unixsocketperm", "requirepass", "rename-command"]
	mongodbDefault = []
	nginxDefault = []
	sparkDefault = []
	tomcatDefault = ["Server"]
	wordpressDefault = []
	joomlaDefault = []
	defaultList = [redisDefault, mongodbDefault, nginxDefault, sparkDefault, tomcatDefault, wordpressDefault, joomlaDefault]
	redisSensitive = ["requirepass", "rename-command"]
	mongodbSensitive = []
	nginxSensitive = []
	sparkSensitive = []
	tomcatSensitive = []
	wordpressSensitive = []
	joomlaSensitive = []
	sensitiveList = [redisSensitive, mongodbSensitive, nginxSensitive, sparkSensitive, tomcatSensitive, wordpressSensitive, joomlaSensitive]
	dealingFunc = [dealPass, dealRename]

	app_dict = {}
	temp_dict = {}
	sensitive_dict = {}

	if sys.argv[1] not in app_type:
		print("Application type not found.")
		sys.exit()

	for i in range(len(app_type)):
		app_dict[app_type[i]] = defaultList[i]
		sensitive_dict[app_type[i]] = sensitiveList[i]

	selectedKey = app_dict[sys.argv[1]]
	sensitiveInfo = sensitive_dict[sys.argv[1]]

	with open("./conftest/server-conf.json") as f:
		data = json.load(f)
		for element in selectedKey:
			try:
				if element in sensitiveInfo:
					temp_dict[element] = dealingFunc[sensitiveInfo.index(element)](data[element])
				else:
					temp_dict[element] = data[element]
			except:
				continue
	with open("./conftest/server-conf-selected.json","w") as target:
		json.dump(temp_dict,target)

if __name__ == "__main__":
	main()
