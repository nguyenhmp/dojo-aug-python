# from (filename) import spaceneedle
class Human(object):
	def __init__(self):
		self.name = "minh"
	def __unicode__(self):
		print "name", self.name
	# def __str__(self):
	# 	string = "human object. Name:" + self.name
	# 	return string
	# 	print "human object"
	# 	print "name:", self.name

# person = Human()
# print person
# print dir(person)
# print person.__unicode__()

# def varargs(arg1, *arg2):
# 	if arg2 == ():
# 		print "i only got one argument"
# 	else:
# 		print "arg2 is of " + str(type(arg2))
# 		print arg2[0]
# # varargs("one")
# varargs("one", "two", "three")
# if ():
# 	daflsjdklf
# else:
# 	dakfj
# y = lambda x : x ** 2
def y(x):
	return x ** 2

squared = y(5)
print squared

