import json
temp_dict = {}
with open("./conftest/redis.conf","r") as file:#add file name as the first parameter
	content = file.readlines()
	for lines in content:
		if lines.strip() != ''  and lines[0] != '#':
			result = lines.find(" ")
			end = lines.find("\n")
			temp_dict[lines[:result]] = lines[result+1:end]
with open("./conftest/redis-conf.json","w") as targetfile:
	json.dump(temp_dict,targetfile)