def outer(func):
	def inner():
		print ("inner is start ")
		func()
		print ("inner is stop")
	return inner

@outer #name()=outer(name)
def name():
	print ("i know decorations")

#print (outer(name))
print ( outer(name)())
print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
name()
