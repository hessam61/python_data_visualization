from random import choice
import matplotlib.pyplot as plt

class RandomWalk():

	def __init__(self, num_points=10000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def walk_fill(self):
		while len(self.x_values) < self.num_points:
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction * x_distance

			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance

			#ignore moves that are not moving
			if x_step == 0 and y_step == 0:
				continue

			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			#print(x_step, ' ', self.x_values[-1],' ', next_x, '\n')

			self.x_values.append(next_x)
			self.y_values.append(next_y)

#Making Random Walks
while True:	
	random_walk = RandomWalk()
	random_walk.walk_fill()
	#set the screen size
	plt.figure(figsize=(10, 6))

	point_numbers = list(range(random_walk.num_points))
	plt.scatter(random_walk.x_values, random_walk.y_values, c=point_numbers, cmap=plt.cm.Reds,
        edgecolor='none', s=5)
	#Display start and end of the walk in different color and size
	plt.scatter(0, 0, c='green', edgecolors='none', s=40)
	plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='blue', edgecolors='none', s=40)
	
	plt.show()

	continue_rw = input("Do you want another walk graph? (y/n): ")
	if continue_rw == 'n':
		break