import json
class Jsonable:
	def json_dump(name,indentt):
		a = locals()
		return json.dumps({'name':a['name'],'type':'Panda'},indent = indentt)
	def json_loads(string):
		return json.loads(string)