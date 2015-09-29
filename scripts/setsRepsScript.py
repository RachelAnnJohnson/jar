from __future__ import print_function

class SetsReps:
	def __init__(self, set_type, arr):
		self.set_type = set_type
		self.arr = arr

	def displaySetsReps(self):
		print ('{ "setType" : "', self.set_type, '", "setsReps" : ' , self.arr, '},', sep='')


SetsReps('light', '["3x20", "3x15", "3x12", "3x8", "3x5", "4x15", "4x12", "4x10"]').displaySetsReps()
SetsReps('heavy', '["4x8", "4x6", "5x10", "5x8", "5x5", "8x8"]').displaySetsReps()
SetsReps('pyramid', '["20, 15, 12, 10, 8, 5, 1", "15, 12, 9, 6, 3", "12, 10, 10, 8, 8, 5"]').displaySetsReps()