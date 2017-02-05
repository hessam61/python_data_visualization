from random import randint
import pygal

class Die():
	"""A class representing a single die."""
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)

die1 = Die()
die2 = Die()

results = []
for roll_number in range(10000):
	result = die1.roll() + die2.roll()
	results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
#if 6-sided die, range between 2 and 12
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results.
histogram = pygal.Bar()
histogram.title = "Results of rolling two 6-sided dice 1000 times."
histogram.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
histogram.x_title = "Result"
histogram.y_title = "Frequency of Result"
histogram.add('two Six-sided dice', frequencies)
histogram.render_to_file('die_visual.svg')


print(frequencies)