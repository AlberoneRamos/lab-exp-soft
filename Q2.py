import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalPullRequests = 0
totalNodes = 0

for node in data:
  totalPullRequests += node["pullRequests"]["totalCount"] 
  totalNodes += 1


print("{:.1f}".format(totalPullRequests / totalNodes))

# Resposta: Tem, em média, 1322.5 Pull requests. Sim, recebem muita contribuição externa