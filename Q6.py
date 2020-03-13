import json
import matplotlib.pyplot as plt
import statistics

with open('output.json', 'r') as file:
  data = json.load(file)

totalNodes = 0
totalIssuesMedian = statistics.median([row['issues']['totalCount'] for row in data])
closedIssuesMedian = statistics.median([row['closedIssues']['totalCount'] for row in data])

totalIssues = sum(row['issues']['totalCount'] for row in data)
totalClosedIssues = sum(row['closedIssues']['totalCount'] for row in data)
print(totalIssues)

# Possuem 86% das issues fechadas em média.
print((totalClosedIssues / totalIssues) * 100)
# Utilizando mediana para calcular, possuem 78% das issues fechadas.
print((closedIssuesMedian / totalIssuesMedian) * 100)

