import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalReleases = 0
totalNodes = 0

for node in data:
  totalReleases += node["releases"]["totalCount"] 
  totalNodes += 1


print("{:.1f}".format(totalReleases / totalNodes))
# 37.2 Releases no total em média. Sabendo, da questão 1, que têm, em média, 5.5 anos.

print("{:.1f}".format((totalReleases / totalNodes) / (5.5 * 12)))
# A cada mês, são lançadas "0.6 releases". No entanto, como não existe meia release. São lan-
# çadas, aproximadamente, 1 release a cada bimestre.