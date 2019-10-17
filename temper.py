import os
import json

p = os.listdir('data/')
d = {}

for a in p:
    d[a[:-4]] = 'data/{}'.format(a)

# print(d)
json.dump(d, open('files.json','w+'))
