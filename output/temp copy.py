import json
import urllib.request
url_list=['https://opentdb.com/api.php?amount=15&type=multiple','https://opentdb.com/api.php?amount=15&category=18&type=multiple','https://opentdb.com/api.php?amount=15&category=9&type=multiple']
url_list_names=['All category','Computers','GK']

data=[]
for i in range (3):
    data.append(urllib.request.urlopen(url_list[i]).read().decode())

#print (data)
obj0 = json.loads(data[0])
print (obj0)
print (type(obj0))
