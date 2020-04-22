import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ['x_value', 'total_1', 'total_2']

# Set the column names
with open('9_data.csv', 'w') as csv_f:
	csv_writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
	csv_writer.writeheader()

# Append random numbers by row
while True:

	with open('9_data.csv', 'a') as csv_f:
		csv_writer = csv.DictWriter(csv_f, fieldnames=fieldnames)

		info = {
			"x_value": x_value,
			"total_1": total_1,
			"total_2": total_2
		}

		csv_writer.writerow(info)
		print(x_value, total_1, total_2)

		x_value += 1
		total_1 += random.randint(-6, 8)
		total_2 += random.randint(-5, 6)

	time.sleep(1)