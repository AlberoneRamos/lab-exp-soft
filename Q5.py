import json
import matplotlib.pyplot as plt


with open('output.json', 'r') as file:
  data = json.load(file)

languages = {}

for node in data:
  primaryLanguage = node.get('primaryLanguage')
  if primaryLanguage is not None:
    languages[primaryLanguage.get('name')] = languages.get(primaryLanguage.get('name'), 0) + 1

languages = { language: languages.pop(language, None) for language in list(languages) if languages[language] > 5}

plt.bar(range(len(languages)), list(languages.values()), align='center')
plt.xticks(range(len(languages)), list(languages.keys()))

plt.show()

print(languages) 

