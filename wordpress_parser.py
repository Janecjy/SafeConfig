import json

lines = []
pub_data = {}
with open('../conftest/wp-config.php','r') as f:
    lines = f.readlines()

def add_define_data(test_line):
    x = test_line.split('(')
    test_line = x[1].split(')')[0]
    a = test_line.split(',')
    a[0] = a[0].strip()
    a[1] = a[1].strip()
    a[0] = a[0].strip("'")
    a[1] = a[1].strip("'")
    pub_data[a[0]] = a[1]

pub_data = {}
for l in lines:
    if 'define(' in l:
        add_define_data(l)
    if '$table_prefix' in l:
        #print('In here')
        a = l.split('=')
        #print(a[1])
        x = a[1].strip()
        #print(x)
        x = x.strip(';')
        #print(x)
        if x == "'wp_'":
            pub_data['prefix_changed'] = 'False'
        else:
            pub_data['prefix_changed'] = 'True'

with open('data.json', 'w') as fp:
    json.dump(pub_data, fp)
