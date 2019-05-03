import sys
import json
import redisfilter
import mongodbfilter
import nginxfilter
import sparkfilter
import tomcatfilter
import wordpressfilter
import joomlafilter

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

def main():
	app_type = ["redis", "mongodb", "nginx", "spark", "tomcat", "wordpress", "joomla"]
	app_dict = {key: eval(key+"filter") for key in app_type}

	temp_dict = {}
	flat_dict = {}

	if sys.argv[1] not in app_type:
		print("Application type not found.")
		sys.exit()

	result_dict = app_dict[sys.argv[1]].init()
	selectedKey = result_dict["default"]
	sensitiveInfo = result_dict["sensitive"]
	dealingFunc = result_dict["dealingFunc"]

	json_file_name = "./conftest/" + sys.argv[1] + "-conf.json"
	json_file_output_name = "./conftest/" + sys.argv[1] + "-conf-selected.json"

	with open(json_file_name) as f:
		data = json.load(f)
		extract_info(data, selectedKey, sensitiveInfo, temp_dict, dealingFunc, flat_dict)

	with open(json_file_output_name,"w") as target:
		json.dump(temp_dict,target)

if __name__ == "__main__":
	main()
