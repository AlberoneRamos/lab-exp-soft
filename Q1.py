import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalTime = sum(time.mktime(time.strptime(node["createdAt"], "%Y-%m-%dT%H:%M:%SZ")) for node in data)
# Tempo médio
avgTime = (totalTime / len(data))

# Tempo médio - 31557600 (60 segundos * 60 minutos * 24 horas * 365.25 dias) = ano
print("{:.1f}".format((time.time() - avgTime)/ 31557600)) 

# Resposta: Tem, em média, 5.5 anos de criação. Maduros