import csv
import numpy as np

# Import census data from CSV
with open('table2j_edu_income _python.csv', 'r') as f:
	my_reader = csv.reader(f)
	data = list(my_reader)

# Find mean

mean = 0

for i in range(0, len(data)):
	mean = mean + int(data[i][1])

mean = mean / (len(data))

print ('Mean: ' + repr(mean))

# Find standard deviation

stdData = []

for i in range (0, len(data)):
	stdData.append(data[i][1])

stdData = list(map(int, stdData))
stdDev = round(np.std(stdData), 3)
print ('Standard deviation: ' + repr(stdDev))
