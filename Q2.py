import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalPullRequests = sum(node["pullRequests"]["totalCount"] for node in data)
print("{:.1f}".format(totalPullRequests / len(data)))

# Resposta: Tem, em média, 1322.5 Pull requests. Sim, recebem muita contribuição externa