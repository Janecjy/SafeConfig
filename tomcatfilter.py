def dealContext(secret):
	return "******"

def init():
	app_dict = {}
	tomcatDefault = ["@shutdown", "@SSLEnabled", "web-resource-name", "url-pattern", "transport-guarantee"]
	tomcatSensitive = ["web-resource-name", "transport-guarantee"]
	tomcatDealingFunc = [dealContext, dealContext]
	app_dict["default"] = tomcatDefault
	app_dict["sensitive"] = tomcatSensitive
	app_dict["dealingFunc"] = tomcatDealingFunc
	return app_dict
