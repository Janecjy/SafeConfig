import xmltodict
import json

with open('./conftest/server.xml') as server_fd:
    server_doc = xmltodict.parse(server_fd.read())

with open('./conftest/web.xml') as web_fd:
    web_doc = xmltodict.parse(web_fd.read())

doc = {}
doc['server'] = server_doc['Server']
doc['web-app'] = web_doc['web-app']

with open("./conftest/tomcat-conf.json","w") as targetfile:
	json.dump(doc,targetfile)
