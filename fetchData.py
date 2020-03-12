import requests
import json
import os
import errno
import time

from string import Template
# RQ01 - Sistemas populares são maduros/antigos?
headers = {'Authorization': 'Bearer 40af6ee2619ba845d74c590cf5ad701d1af9e25f'}


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
      if request.status_code == 502:
          return run_query(query)
      else:
        raise Exception('Error {}. {}'.format(request.status_code, query))


query = Template('''
{
  search(query: "stars:>100", type: REPOSITORY, first: 10$after) {
    pageInfo {
        hasNextPage,
        endCursor
    },
    nodes {
      ... on Repository {
        nameWithOwner,
        createdAt,
        updatedAt,
        primaryLanguage {
          name
        },
        closedIssues: issues(states: CLOSED) {
          totalCount
        },
        issues {
          totalCount
        },
        stargazers {
          totalCount
        },
        pullRequests (states: MERGED){
          totalCount
        },
        releases {
          totalCount
        }
      }
    }
  }
}
''')

filename = 'output.json'
result = run_query(query.substitute(after=''))
nodes = []

print(result)
hasNextPage = result['data']['search']['pageInfo']['hasNextPage']
cursor = result['data']['search']['pageInfo']['endCursor']
for node in result['data']['search']['nodes']:
    nodes.append(node)

while hasNextPage:
  result = run_query(query.substitute(after=', after: \"%s\"' % cursor))
  print('Result - {}'.format(result))
  cursor = result['data']['search']['pageInfo']['endCursor']
  hasNextPage = result['data']['search']['pageInfo']['hasNextPage']
  for node in result['data']['search']['nodes']:
    nodes.append(node)

with open('output.json', 'w') as file:
  file.write(json.dumps(nodes))

print('Written to file output.json')