def memoize(f):
	cache = {}
	def cached_func(n):
		if n in cache:
			return cache[n]
		else:
			cache[n] = f(n)
			return cache[n]
	return cached_func

@memoize
def fact(n):
	if n < 2:
		return 1
	else:
		return n*fact(n-1)


for i in range(1000):
	print(fact(i))
