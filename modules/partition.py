import os
import math

class PartitionInfo:
	# Private member variables
	_total = 0
	_free = 0
	_used = 0
	_path = ""

	def __init__(self, path):
		self._path = path
		self.update()

	def is_mounted(path):
		#This function will check volume name is mounted or not.  
		return True if os.path.ismount(path) == True else False

	def set_path(self, path):
		if is_mounted() == False:
			return False
		else:
			self.update()
			return True

	def update(self):
		st = os.statvfs(self._path)
		self._total = st.f_blocks * st.f_frsize
		self._free = st.f_bfree * st.f_frsize
		self._used = self._total - self._free
		#print("Total:{0:d}, Free:{0:d}. Used:{0:d}".format(self._total, self._free, self._used))

	def get_free_space(self):
		return self._free

	def get_total_space(self):
		return self._total

	def get_used_space(self):
		return self._used

	def get_capacity(self):
		return 0 if self._total == 0 else math.ceil(( self._used / self._total ) * 100)
