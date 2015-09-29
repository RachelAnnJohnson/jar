from __future__ import print_function

class Workout:
	def __init__(self, body_part, exercise, **kwargs):
		self.body_part = body_part
		self.exercise = exercise
		for key in kwargs.iteritems():
			print key

	def displayWorkout(self):
		print ('{ "bodyPart" : "', body_part, '", "exercise" : "' , self.exercise, '"},', sep='')

class WorkoutVarOne:
	def __init__(self, body_part, exercise, variation_one, variation_one_arr):
		self.body_part = body_part
		self.exercise = exercise
		self.variation_one = variation_one
		self.variation_one_arr = variation_one_arr

	def displayWorkout(self):
		print ('{ "bodyPart" : "', self.body_part, '", "exercise" : "' , self.exercise, '", "variations" : { "', self.variation_one, '" : ', self.variation_one_arr,'}},', sep='')

class WorkoutVarTwo:
	def __init__(self, body_part, exercise, variation_one, variation_one_arr, variation_two, variation_two_arr):
		self.body_part = body_part
		self.exercise = exercise
		self.variation_one = variation_one
		self.variation_one_arr = variation_one_arr
		self.variation_two = variation_two
		self.variation_two_arr = variation_two_arr

	def displayWorkout(self):
		print ('{ "bodyPart" : "', self.body_part, '", "exercise" : "' , self.exercise, '", "variations" : { "', self.variation_one, '" : ', self.variation_one_arr,', "', self.variation_two, '" : ', self.variation_two_arr, '}},', sep='')

class WorkoutVarThree:
	def __init__(self, body_part, exercise, variation_one, variation_one_arr, variation_two, variation_two_arr, variation_three, variation_three_arr):
		self.body_part = body_part
		self.exercise = exercise
		self.variation_one = variation_one
		self.variation_one_arr = variation_one_arr
		self.variation_two = variation_two
		self.variation_two_arr = variation_two_arr
		self.variation_three = variation_three
		self.variation_three_arr = variation_three_arr

	def displayWorkout(self):
		print ('{ "bodyPart" : "', self.body_part, '", "exercise" : "' , self.exercise, '", "variations" : { "', self.variation_one, '" : ', self.variation_one_arr,', "', self.variation_two, '" : ', self.variation_two_arr,', "', self.variation_three, '" : ', self.variation_three_arr, '}},', sep='')

stance = '["wide-stance", "narrow-stance", "neutral-stance"]'
toes = '["toes angled inward", "toes angled outward", "toes straight ahead"]'
grip = '["wide-grip", "neutral-grip", "close-grip", "reverse-grip"]'
bench = '["incline", "decline", "flat"]'
weightType = '["dumbbell", "barbell"]'
position = '["standing", "seated"]'

WorkoutVarOne('legs', 'hack squat', 'stance' = '["regular", "reverse"]').displayWorkout()

# Workout('legs', 'front squat').displayWorkout()
# Workout('legs', 'goblet squat').displayWorkout()
# Workout('legs', 'good mornings').displayWorkout()
# Workout('legs', 'curtsy squats').displayWorkout()
# Workout('legs', 'leg extension').displayWorkout()
# Workout('legs', 'leg curl').displayWorkout()
# Workout('legs', 'hip abduction machine').displayWorkout()
# Workout('legs', 'hip adduction machine').displayWorkout()
# Workout('legs', 'single leg squats using bench').displayWorkout()
# WorkoutVarOne('legs', 'hack squat', 'stance', '["regular", "reverse"]').displayWorkout()
# WorkoutVarOne('legs', 'split squats', 'weightType', weightType).displayWorkout()
# WorkoutVarOne('legs', 'back squat', 'stance', '["narrow-stance", "wide-stance", "neutral-stance", "heels elevated on plate"]').displayWorkout()
# WorkoutVarOne('legs', 'leg press', 'stance', stance).displayWorkout()
# WorkoutVarOne('legs', 'stiff legged deadlift', 'weightType', weightType).displayWorkout()
# WorkoutVarOne('legs', 'deadlift', 'weightType', '["dumbbell", "barbell"]').displayWorkout()
# WorkoutVarOne('legs', 'romanian deadlift', 'weightType', weightType).displayWorkout()
# WorkoutVarOne('legs', 'sumo deadlift', 'weightType', weightType).displayWorkout()
# WorkoutVarTwo('legs', 'lunges', 'stance', '["walking", "standing"]', 'weightType', weightType).displayWorkout()

# Workout('glutes', 'wide-stance back squat').displayWorkout()
# Workout('glutes', 'hip abduction machine').displayWorkout()
# Workout('glutes', 'good mornings').displayWorkout()
# WorkoutVarOne('glutes', 'stiff legged deadlift', 'weightType', weightType).displayWorkout()
# WorkoutVarOne('glutes', 'glute kickback', 'weightType', '["machine", "cable"]').displayWorkout()

# WorkoutVarTwo('calves', 'donkey calf raise', 'stance', stance, 'toes', toes).displayWorkout()
# WorkoutVarTwo('calves', 'seated calf raise', 'stance', stance, 'toes', toes).displayWorkout()
# WorkoutVarTwo('calves', 'calf raise on smith machine using platform', 'stance', stance, 'toes', toes).displayWorkout()
# WorkoutVarTwo('calves', 'standing calf raise machine', 'stance', stance, 'toes', toes).displayWorkout()
# WorkoutVarTwo('calves', 'calf raise on leg press', 'stance', stance, 'toes', toes).displayWorkout()

# WorkoutVarOne('back', 'pullups', 'grip', grip).displayWorkout()
# WorkoutVarOne('back', 'lat pulldowns', 'grip', grip).displayWorkout()
# WorkoutVarTwo('back', 'rows', 'grip', grip, 'weightType', '["barbell", "dumbbell", "cable", "single arm cable", "single arm dumbbell"]').displayWorkout()

# Workout('chest', 'dips').displayWorkout()
# Workout('chest', 'svend press').displayWorkout()
# WorkoutVarOne('chest', 'pushups', 'grip', '["wide-grip", "neutral-grip", "close-grip"]').displayWorkout()
# WorkoutVarTwo('chest', 'chest flyes','weightType', '["dumbbell", "cable"]', 'benchType', bench, ).displayWorkout()
# WorkoutVarThree('chest', 'press', 'grip', grip, 'weightType', '["barbell", "dumbbell"]', 'benchType', bench).displayWorkout()

# Workout('biceps', 'zottoman curls').displayWorkout()
# Workout('biceps', 'hammer curls').displayWorkout()
# WorkoutVarOne('biceps', 'preacher curls', 'weightType', weightType).displayWorkout()
# WorkoutVarTwo('biceps', 'curls', 'weightType', '["barbell", "dumbbell", "ez bar", "cable"]', 'grip', grip).displayWorkout()

# WorkoutVarOne('triceps', 'dips', 'type', '["machine", "bench", "regular"]').displayWorkout()
# WorkoutVarOne('triceps', 'dips', 'type', '["machine", "bench", "regular"]').displayWorkout()
# WorkoutVarOne('triceps', 'french press', 'position', position).displayWorkout()
# WorkoutVarOne('triceps', 'tricep pushdown', 'weightType', '["cable straight bar", "cable rope"]').displayWorkout()
# WorkoutVarOne('triceps', 'skullcrushers', 'grip', '["wide-grip", "neutral-grip", "close-grip"]').displayWorkout()
# WorkoutVarTwo('triceps', 'tricep extension', 'position', position, 'weightType', '["dumbbell", "barbell", "cable straight bar", "cable rope"]').displayWorkout()

# WorkoutVarOne('shoulders', 'rear delt flyes', 'weightType', '["dumbbell", "cable", "machine"]').displayWorkout()
# WorkoutVarTwo('shoulders', 'side raises', 'weightType', '["dumbbell", "cable"]', 'position', position).displayWorkout()
# WorkoutVarTwo('shoulders', 'press', 'type', '["military", "dumbbell shoulder", "barbell shoulder"]', 'position', position).displayWorkout()
# WorkoutVarTwo('shoulders', 'front raises', 'weightType', '["dumbbell", "barbell", "cable", "plate"]', 'position', position).displayWorkout()