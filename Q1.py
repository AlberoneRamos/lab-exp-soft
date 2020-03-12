import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalTime = 0
totalNodes = 0

for node in data:
  totalTime += time.mktime(time.strptime(node["createdAt"], "%Y-%m-%dT%H:%M:%SZ"))
  totalNodes += 1

# Tempo médio
avgTime = (totalTime / totalNodes)

# Tempo médio - 31557600 (60 segundos * 60 minutos * 24 horas * 365.25 dias) = ano
print("{:.1f}".format((time.time() - avgTime)/ 31557600)) 

# Resposta: Tem, em média, 5.5 anos de criação. Maduros