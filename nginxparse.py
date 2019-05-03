import json

dic_index = 0
original_dic ={}
temp_dict = original_dic
dics = [original_dic]
with open("./conftest/nginx.conf","r") as file:#add file name as the first parameter
	content = file.readlines()
	for lines in content:
		if lines.strip() != ''  and lines.find('#') == -1:

			#Deal with nesting
			if lines.find('{') != -1:
				striped_line = lines.strip()
				result =striped_line.find("{", 0)
				new_dict = {}
				temp_dict[striped_line[:result]] = new_dict
				temp_dict = new_dict
				dic_index+=1
				dics.append(temp_dict)
				continue
			if lines.find('}') != -1:
				striped_line = lines.strip()
				result =striped_line.find("}", 0)
				dic_index-=1
				temp_dict = dics[dic_index]
				continue

			striped_line = lines.strip()
			result =striped_line.find(" ", 0)
			temp_dict[striped_line[:result]] = striped_line[result+1:]


with open("./conftest/nginx-conf.json","w") as targetfile:
	json.dump(original_dic,targetfile)
