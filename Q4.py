import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalTime = 0
totalNodes = 0

for node in data:
  totalTime += time.mktime(time.strptime(node["updatedAt"], "%Y-%m-%dT%H:%M:%SZ"))
  totalNodes += 1

# Tempo médio
avgTime = (totalTime / totalNodes)

# Tempo atual - tempo médio divido por (60 segundos * 60 minutos) = hora
print("{:.1f}".format((time.time() - avgTime)/ (60 * 60))) 

# Resposta: Foram atualizados há, em média, 1 hora e 30 minutos de agora