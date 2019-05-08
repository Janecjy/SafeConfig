def mongo_attester(filename):
    with open(filename,'r') as f:
        temp = json.load(f)
    isSecure = False
    for k in temp.keys():
        isSecure = isSecure&temp[k]
    return isSecure
