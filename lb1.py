import csv
with open('wine.data', 'r') as f:
    wines = list(csv.reader(f))
for j in range(1, 14):
    scores = [float(i[j]) for i in wines]
    sum_score = sum(scores)
    num_score = len(scores)
    m = sum(scores) / len(scores)
    var_res = sum((xi - m) ** 2 for xi in scores) / len(scores)
print(var_res)



