import json
import matplotlib.pyplot as plt


with open('output.json', 'r') as file:
  data = json.load(file)

totalTime = 0
totalNodes = 0

languages = {}

for node in data:
  primaryLanguage = node.get('primaryLanguage')
  if primaryLanguage is not None:
    languages[primaryLanguage.get('name')] = languages.get(primaryLanguage.get('name'), 0) + 1
  totalNodes += 1

# Tempo atual - tempo médio divido por (60 segundos * 60 minutos) = hora
print(languages) 

# Resposta: Foram atualizados há, em média, 1 hora e 30 minutos de agora