import csv
import numpy as np

# Import census data from CSV
with open('table2a_2j_correlations_python_improved.csv', 'r') as f:
	my_reader = csv.reader(f)
	data = list(my_reader)

# Find mean

mean = 0

for j in range(0, 2):
	for i in range(0, len(data)):
		mean = mean + int(data[i][j])

mean = mean / (len(data) * 2)

print ('Mean: ' + repr(mean))

# Find standard deviation

stdData = []

for j in range(0, 2):
	for i in range (0, len(data)):
		stdData.append(data[i][j])

stdData = list(map(int, stdData))
stdDev = round(np.std(stdData), 3)
print ('Standard deviation: ' + repr(stdDev))
