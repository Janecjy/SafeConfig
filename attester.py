import json
'''
    Function that tells you whether a json file describes a secure
    config.
'''

'''
    Come up with a common definition for "secure" config
'''
def attest_config(filename):
    security_data = {}
    score = 0
    with open(filename) as json_file:  
        security_data = json.load(json_file)
        
        
    