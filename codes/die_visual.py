import pygal
from die import Die


# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
#print(results)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)

# Visualize the result
hist = pygal.Bar()
hist.title = "Result of rolling two D6 dice 1000 times."
hist.x_labels = [x for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_vusual4.svg')

