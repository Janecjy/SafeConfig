import json

def main():
	secure = True
	tomcatDefault = ["@shutdown", "@SSLEnabled", "web-resource-name", "url-pattern", "transport-guarantee", "http-only", "secure"]
	tomcatSensitive = ["web-resource-name", "transport-guarantee"]
	with open("./conftest/tomcat-conf-selected.json","r") as file:
		data = json.load(file)
		for key in tomcatDefault:
			if key not in data:
				secure = False
			else:
				if key == "http-only" and data[key] != "true":
					secure = False
				if key == "secure" and data[key] != "true":
					secure = False
				if key in tomcatSensitive and "*" not in data[key]:
					secure = False
	return secure

if __name__ == "__main__":
	main()