import requests
import json
import os
import errno

from string import Template
# RQ01 - Sistemas populares são maduros/antigos?
headers = {'Authorization': 'Bearer cd442252f1781447e0547f1c75ebcbfc79900431'}


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
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

filename = 'output.csv'
result = run_query(query.substitute(after=''))
print(result)
hasNextPage = result['data']['search']['pageInfo']['hasNextPage']
cursor = result['data']['search']['pageInfo']['endCursor']
nodes = result['data']['search']['nodes']

while hasNextPage:
  result = run_query(query.substitute(after=', after: \"%s\"' % cursor))
  print('Result - {}'.format(result))
  cursor = result['data']['search']['pageInfo']['endCursor']
  hasNextPage = result['data']['search']['pageInfo']['hasNextPage']
  nodes += result['data']['search']['nodes']

for node in nodes:
  with open(filename, 'a') as file:
    file.write(node['nameWithOwner'] + '\n')
print('Written to file RQ01-answer.json')