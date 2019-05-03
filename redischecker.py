import json

def main():
	secure = True
	redisDefault = ["bind", "protected-mode", "port", "unixsocketperm", "requirepass", "rename-command"]
	redisSensitive = ["requirepass", "rename-command"]
	with open("./conftest/redis-conf-selected.json","r") as file:
		data = json.load(file)
		for key in redisDefault:
			if key not in data:
				secure = False
			else:
				if key in redisSensitive and "*" not in data[key]:
					secure = False
	return secure

if __name__ == "__main__":
	main()