import random
def func(args):
	def sum():
		ax=0
		for i in args:
			ax+=i
		return ax
	return sum
a=func(list(range(6)))
b=func(list(range(6)))
print (a)
print(b)
