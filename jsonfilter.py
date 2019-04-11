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
	tomcatDefault = []
	wordpressDefault = []
	joomlaDefault = []
	defaultList = [redisDefault, mongodbDefault, nginxDefault, sparkDefault, tomcatDefault, wordpressDefault, joomlaDefault]
	sensitiveInfo = ["requirepass", "rename-command"]
	dealingFunc = [dealPass, dealRename]

	app_dict = {}
	temp_dict = {}

	if sys.argv[1] not in app_type:
		print("Application type not found.")
		sys.exit()

	for i in range(len(app_type)):
		app_dict[app_type[i]] = defaultList[i]

	selected = app_dict[sys.argv[1]]

	with open("./redis-conf.json") as f:
		data = json.load(f)
		for element in selected:
			try:
				if element in sensitiveInfo:
					temp_dict[element] = dealingFunc[sensitiveInfo.index(element)](data[element])
				else:
					temp_dict[element] = data[element]
			except:
				continue
	with open("./redis-conf-selected.json","w") as target:
		json.dump(temp_dict,target)

if __name__ == "__main__":
	main()
