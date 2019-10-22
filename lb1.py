import csv
import statistics
import math

# data set "wine" has been converted to a list
with open('wine.data', 'r') as f:
    wines = list(csv.reader(f))
#avg value of each attribute
avg_list = []
for j in range(1, 14):
    avg = [float(i[j]) for i in wines]
    sum_score = sum(avg)
    num_score = len(avg)
    avg_list.append(sum_score/num_score)
print(avg_list)
#medain for each attribute
median_list = []
for j in range(1, 14):
    median = [float(i[j]) for i in wines if i[j] != ""]
    num_wines = len(median)
    sorted_prices = sorted(median)
    median_list.append(statistics.median(sorted_prices))
print(median_list)
#minimum and maximum for each attribute
min_score = []
max_score = []
for j in range(1, 14):
    scores = [float(i[j]) for i in wines if i[j] != ""]
    max_score.append(max(scores))
    min_score.append(min(scores))
print(min_score, '\n', max_score)
#dispersion for each attribute
dis_list = []
for j in range(1, 14):
    scores = [float(i[j]) for i in wines]
    sum_score = sum(scores)
    num_score = len(scores)
    m = sum(scores) / len(scores)
    dis_list.append(sum((xi - m) ** 2 for xi in scores) / len(scores))
print(dis_list)
#standard deviation for each attribute
deviation_list = []
for j in range(1, 14):
    deviation = [float(i[j]) for i in wines]
    sum_score = sum(deviation)
    num_score = len(deviation)
    m = sum(deviation) / len(deviation)
    deviation_list.append(math.sqrt(sum((xi - m) ** 2 for xi in deviation) / len(deviation)))
print(deviation_list)
#scope for each attribute
scope = []
for j in range(1, 14):
    scores = [float(i[j]) for i in wines]
    scope.append(max(scores) - min(scores))
print(scope)
#half sum for each attribute
hsum_list = []
for j in range(1, 14):
    hsum = [float(i[j]) for i in wines]
    hsum_list.append((max(hsum) + min(hsum)) / 2)
print(hsum_list)


from pandas import read_csv
wine=read_csv('wine.data',header=None)
import math

avg_module = {}
avg_atr={}
for key in wine:
    avg_atr[key] = wine[key].mean()
    sum_of_modules=0
    arr_temp = []
    for key2 in wine[key]:
        arr_temp.append(key2)
        sum_of_modules+=math.fabs(key2-avg_atr[key])
    avg_module[key] = sum_of_modules / len(wine[key])
print(avg_module)
