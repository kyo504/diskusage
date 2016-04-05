import threading

'''
Javascipt-like SetInterval function using Decorator Functions with Arguments

Reference to implement this feature
- About decorator : http://thecodeship.com/patterns/guide-to-python-function-decorators/
                  : http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html
- About threading : https://docs.python.org/2/library/threading.html
'''
def set_interval(interval):
	# This will be the actual decorator with fixed interval
	def decorator(function):
		# This will be the function to be called
		def wrapper(*args, **kwargs):
			# A factory function that returns a new event object. 
			# An event manages a flag that can be set to true with the set() method
			stopped = threading.Event()

			def loop(): # excuted in another thread
				while not stopped.wait(interval): # Run loop until stopped by calling set()
					function(*args, **kwargs)

			t = threading.Thread(target=loop)
			t.daemon = True # stop if the program exits
			t.start()
			return stopped
		return wrapper
	return decorator

'''
Another implementaion of Javascript-like SetInterval
'''
def call_repeatedly(interval, func, *args):
	stopped = threading.Event()
	def loop():
		while not stopped.wait(interval): # the first call is in `interval` secs
			func(*args)
	t = threading.Thread(target=loop)
	t.daemon = True
	t.start()    
	return stopped.set
