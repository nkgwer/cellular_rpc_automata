import matplotlib.pyplot as plt
import csv
start = 0
end = 400
red_result = []
green_result = []
yellow_result = []
plt.figure(figsize=(16, 3))
with open('result.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        red_result.append(row[0])
        green_result.append(row[1])
        yellow_result.append(row[2])

x = range(len(red_result[start:end]))
plt.plot(x, red_result[start:end], color='red')
plt.plot(x, green_result[start:end], color='green')
plt.plot(x, yellow_result[start:end], color='yellow')
plt.savefig('graph.jpg', dpi=400)