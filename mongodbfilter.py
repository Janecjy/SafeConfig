def init():
	app_dict = {}
	mongodbDefault = []
	mongodbSensitive = []
	mongodbDealingFunc = []
	app_dict["default"] = mongodbDefault
	app_dict["sensitive"] = mongodbSensitive
	app_dict["dealingFunc"] = mongodbDealingFunc
	return app_dict

import yaml
import json

def mongodb_security_check(filename):
    stream = open(filename, 'r')
    conf = yaml.load(stream)
    cmds = conf['spec']['template']['spec']['containers'][0]['command']

    if not 'mongod' in cmds:
        print("no command specified")
    network_restrictions = False
    if '--bind_ip' in cmds:
        network_restrictions = True

    access_ctrl = False
    if '--auth' in cmds:
        access_ctrl = True

    #checks if ssl is and enabled - can add a score or just display param
    encrypted_comm = False
    try :
        ind = cmds.index('--sslmode')
        if not ind is None:
            if(cmds[ind+1]!='disabled'):
                encrypted_comm = True
    except:
        pass
    #Recommended to use x.509
    membership_auth = False
    try :
        ind = cmds.index('--clusterAuthMode')
        if not ind is None:
            if '--sslCAFile' in cmds[ind:]:
                membership_auth = True
    except:
        pass
    
    data_enc = False
    if '--enableEncryption' in cmds:
        data_enc = True

    js_disabled = False

    if '--noscripting' in cmds:
        js_disabled = True
    
    #write info from relevant params to json
    final_dict = {}
    final_dict['network restrictions'] = network_restrictions
    final_dict['access control'] = access_ctrl
    final_dict['encrypted comm'] = encrypted_comm
    final_dict['membership autherization'] = membership_auth
    final_dict['data encryption'] = data_enc
    final_dict['misc'] = js_disabled
