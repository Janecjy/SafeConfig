import xmltodict
import json

with open('./conftest/server1.xml') as fd:
    doc = xmltodict.parse(fd.read())

with open("./conftest/server1-conf.json","w") as targetfile:
	json.dump(doc,targetfile)