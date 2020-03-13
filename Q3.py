import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalReleases = sum(node["releases"]["totalCount"] for node in data)

print("{:.1f}".format(totalReleases / len(data)))
# 37.2 Releases no total em média. Sabendo, da questão 1, que têm, em média, 5.5 anos.

print("{:.1f}".format((totalReleases / len(data)) / (5.5 * 12)))
# A cada mês, são lançadas "0.6 releases". No entanto, como não existe meia release. São lan-
# çadas, aproximadamente, 1 release a cada bimestre.