def timed_func(f, args=(), kwargs={}, timeout=30, default=None, errormsg="Timeout error"):

	import signal
	class TimeoutError(Exception):
		pass

	def timeout_handler(signum, frame):
		raise TimeoutError

  # Register a signal to our handler
	signal.signal(signal.SIGALRM, timeout_handler)

  # Trigger an alarm after timeout seconds
	signal.alarm(timeout)
	
  # Try a function call:
  # If it returns normally before the timeout, pass along the value
  # Otherwise, print the specific error and return the default value
	try:
		result = f(*args, **kwargs)
	except TimeoutError:
		result = default
		print(errormsg)
	finally:
		signal.alarm(0)
		return result

# Silly function that never returns
def forever():
	import time
	while True:
		time.sleep(1)

# Function that may or may not complete depending on the timeout
def andever(a,b):
	result = a
	while True:
		result += b
		#if result > 200000000:
		if result > 100000000:
			return result

# Test
print timed_func(forever, timeout=2, default="no response", errormsg="failed to update")
print timed_func(andever, (1,2), timeout=5, default=-1, errormsg="computation timeout")
