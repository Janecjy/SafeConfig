def init():
	app_dict = {}
	nginxDefault = ["server_tokens", "ssl_protocols", "listen", ]
	nginxSensitive = ["","","ssl_ciphers", "ssl_certificate", "ssl_certificate_key"]
	nginxDealingFunc = []
	app_dict["default"] = nginxDefault
	app_dict["sensitive"] = nginxSensitive
	app_dict["dealingFunc"] = nginxDealingFunc
	return app_dict
