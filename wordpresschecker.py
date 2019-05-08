import json

def main():
	secure = True
	wpDefault = ["bind", "protected-mode", "port", "unixsocketperm", "requirepass", "rename-command"]
	wpSensitive = ["requirepass", "rename-command"]
	with open("./conftest/wordpress-conf-selected.json","r") as file:
		data = json.load(file)
		for key in redisDefault:  
      if key not in data:
				secure = False
			else:
				if key in wpSensitive and "*" not in data[key]:
					secure = False
    if data['prefix_changed']==False:
      return False  
	return secure

if __name__ == "__main__":
	main()
