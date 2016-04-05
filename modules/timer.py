import threading

'''
Decorator Functions with Arguments


Decorator is ideal when you need to extend the functionality of functions that you don't want to modify. 
Essentially, decorators work as wrappers, modifying the behavior of the code 
before and after a target function execution, without the need to modify the function itself, 
augmenting the original functionality, thus decorating it.

Reference to implement this feature
- About Decorator : http://thecodeship.com/patterns/guide-to-python-function-decorators/

'''
def set_interval(interval):
	# This will be the actual decorator with fixed interval
	def decorator(function):
		# This will be the function to be called
		def wrapper(*args, **kwargs):
			stopped = threading.Event()

			def loop(): # excuted in another thread
				while not stopped.wait(interval): # until stopped
					function(*args, **kwargs)

			t = threading.Thread(target=loop)
			t.daemon = True # stop if the program exits
			t.start()
			return stopped
		return wrapper
	return decorator
