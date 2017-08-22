from mako.template import Template
from mako.lookup import TemplateLookup
arg={
	'one' : 1,
	'two' :2,
	'three' :3,
}
args={
	"arg" : arg
}
mylookup = TemplateLookup(directories=['.'])
mytemplate = Template(filename='template1.txt',lookup=mylookup)
print(mytemplate.render(**args))