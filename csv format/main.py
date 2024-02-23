# import numpy as np
#
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
#
# print(a + b)
# print(a.dtype)
#
#
# np.full((1, 2), 55)
# print(np.ones((10, 5, 5)))
import csv
from datetime import datetime

file = open("Google Stock Market Data - google_stock_data.csv.csv", newline="")
reader = csv.reader(file)

header = next(reader)

data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])

print(data[0])

file2 = open("google_returns", 'w')
writer = csv.writer(file2)
writer.writerow(["Date", 'returns'])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i + 1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    # writer.writerow([todays_date, daily_return])
    formatted_date = todays_date.strftime("%m/%d/%Y")
    writer.writerow([formatted_date, daily_return])
