class Underscore(object):
	def __init__(self):
		pass
	def map(self, lis, func):
		newLis = []
		for val in lis:
			newLis.append(func(val))
		return newLis
	def reduce(self, lis, func, memo = 0):
		memo = memo
		for val in lis:
			memo += func(val)
		return memo
	def find(self, lis, cond):
		for val in lis:
			if cond(val):
				return val
		return False
	def filter(self, lis, cond):
		newLis = []
		for val in lis:
			if cond(val):
				newLis.append(val)
		return None if newLis==[] else newLis
	def reject(self, lis, cond):
		newLis = []
		for val in lis:
			if cond(val):
				continue
			newLis.append(val)
		return None if newLis==[] else newLis

_ = Underscore()
