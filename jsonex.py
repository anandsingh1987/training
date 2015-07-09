import json
a=[]
with open("example.json",'r+') as handle:
	parsed=json.load(handle)
	print json.dumps(parsed,indent=4)
	parsed['id']=173
	handle.seek(0)
	a.append(json.dumps(parsed))
	#data=json.JSONEncoder().encode({"foo": ["bar", "baz"]})
	json.dump(parsed,handle,indent=4)

print a[0]

