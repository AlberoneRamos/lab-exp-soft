import json
import datetime
import time

with open('output.json', 'r') as file:
  data = json.load(file)

totalTime = sum(time.mktime(time.strptime(node["updatedAt"], "%Y-%m-%dT%H:%M:%SZ")) for node in data)


# Tempo médio
avgTime = (totalTime / len(dataz))

# Tempo atual - tempo médio divido por (60 segundos * 60 minutos) = hora
print("{:.1f}".format((time.time() - avgTime)/ (60 * 60))) 

# Resposta: Foram atualizados há, em média, 1 hora e 30 minutos de agora