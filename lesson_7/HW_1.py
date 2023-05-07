import csv
from datetime import datetime


source_file = 'test_file.csv'
target_file = 'salaries_uah.csv'
today = datetime.now().date()
exchange_rate = 37.9
with open(source_file, 'r') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

for row in data[1:]:
    for i in range(1, len(row)):
        row[i] = float(row[i]) * exchange_rate

with open(target_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
