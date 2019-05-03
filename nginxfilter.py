def check_ciphers(cipher):
	if len(cipher.replace('+',''))>10:
		return "********"
	else:
		return "NOT SECURE CIPHER"

def check_ssl_cert(cert_location):
	try:
		f = open(cert_location)
		return "*********"
	except FileNotFoundError:
		return "Certificate file does not exist"

def check_ssl_certificate_key(cert_key_location):
	try: 
		f = open(cert_key_location)
		return "*********"
	except FileNotFoundError:
		return "Certificate key file does not exist"

def init():
	app_dict = {}
	nginxDefault = ["server_tokens", "ssl_protocols", "listen"]
	nginxSensitive = ["ssl_ciphers", "ssl_certificate", "ssl_certificate_key"]
	nginxDealingFunc = [check_ciphers, check_ssl_cert, check_ssl_certificate_key]
	app_dict["default"] = nginxDefault
	app_dict["sensitive"] = nginxSensitive
	app_dict["dealingFunc"] = nginxDealingFunc
	return app_dict
