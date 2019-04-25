import sys
import json

def extract_info(obj, keys, sensitive, temp_dict, dealingFunc, flat_dict):
	if isinstance(obj, dict):
		for k, v in obj.items():
			if isinstance(v, (dict, list)):
				extract_info(v, keys, sensitive, temp_dict, dealingFunc, flat_dict)
			else:
				flat_dict[k] = v
				if k in keys:
					if k in sensitive:
						temp_dict[k] = dealingFunc[sensitive.index(k)](v)
					else:
						temp_dict[k] = v
	elif isinstance(obj, list):
		for item in obj:
			extract_info(item, keys, sensitive, temp_dict, dealingFunc, flat_dict)

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

def dealContext(secret):
	return "******"

def main():
	app_type = ["redis", "mongodb", "nginx", "spark", "tomcat", "wordpress", "joomla"]

	redisDefault = ["bind", "protected-mode", "port", "unixsocketperm", "requirepass", "rename-command"]
	mongodbDefault = []
	nginxDefault = ["server_tokens", "ssl_protocols", "listen", ]
	sparkDefault = ["spark.blockManager.port", "spark.driver.blockManager.port", "spark.ssl.enabled", "spark.ssl.[namespace].port", 
	"spark.ssl.enabledAlgorithms", "spark.ssl.needClientAuth"] 
	tomcatDefault = ["@shutdown", "@SSLEnabled", "web-resource-name", "url-pattern", "transport-guarantee"]
	wordpressDefault = []
	joomlaDefault = []
	defaultList = [redisDefault, mongodbDefault, nginxDefault, sparkDefault, tomcatDefault, wordpressDefault, joomlaDefault]
	redisSensitive = ["requirepass", "rename-command"]
	mongodbSensitive = []
	nginxSensitive = ["","","ssl_ciphers", "ssl_certificate", "ssl_certificate_key"]
	sparkSensitive = ["","","spark.ssl.trustStore", "spark.ssl.trustStorePassword"]
	tomcatSensitive = ["web-resource-name", "transport-guarantee"]
	wordpressSensitive = []
	joomlaSensitive = []
	sensitiveList = [redisSensitive, mongodbSensitive, nginxSensitive, sparkSensitive, tomcatSensitive, wordpressSensitive, joomlaSensitive]
	redisDealingFunc = [dealPass, dealRename]
	mongodbDealingFunc = []
	nginxDealingFunc = []
	sparkDealingFunc = []
	tomcatDealingFunc = [dealContext, dealContext]
	wordpressDealingFunc = []
	joomlaDealingFunc = []
	dealingFuncList = [redisDealingFunc, mongodbDealingFunc, nginxDealingFunc, sparkDealingFunc, tomcatDealingFunc, wordpressDealingFunc, joomlaDealingFunc]

	app_dict = {}
	temp_dict = {}
	sensitive_dict = {}
	dealingFunc_dict = {}
	flat_dict = {}

	if sys.argv[1] not in app_type:
		print("Application type not found.")
		sys.exit()

	for i in range(len(app_type)):
		app_dict[app_type[i]] = defaultList[i]
		sensitive_dict[app_type[i]] = sensitiveList[i]
		dealingFunc_dict[app_type[i]] = dealingFuncList[i]

	selectedKey = app_dict[sys.argv[1]]
	sensitiveInfo = sensitive_dict[sys.argv[1]]
	dealingFunc = dealingFunc_dict[sys.argv[1]]

	json_file_name = "./conftest/" + sys.argv[1] + "-conf.json"
	json_file_output_name = "./conftest/" + sys.argv[1] + "-conf-selected.json"

	with open(json_file_name) as f:
		data = json.load(f)
		extract_info(data, selectedKey, sensitiveInfo, temp_dict, dealingFunc, flat_dict)

	# for e in flat_dict:
	# 	print(e)
	# 	print(flat_dict[e])

	with open(json_file_output_name,"w") as target:
		json.dump(temp_dict,target)

if __name__ == "__main__":
	main()
