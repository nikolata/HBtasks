from jsonable import *
class Panda(Jsonable):
	def __init__(self,name = 'marto'):
		if isinstance(name,str) == False:
			raise TypeError('Name needs to be string')
		self.name = name
	def to_json(self,indent = 4):
		if isinstance(indent,int) == False or indent<0:
			raise TypeError('Indent can be only >=0 integer')
		return Jsonable.json_dump(self.name,indent)
	def from_json(self,json_string):
		d =Jsonable.json_loads(json_string)
		p = Panda(d['name'])
		return p
	def __eq__(self,other):
		return self.name == other.name


a = Panda('gosho')
temp = a.to_json()
p = a.from_json(temp)
print(p.name)