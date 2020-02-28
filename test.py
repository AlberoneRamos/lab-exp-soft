import requests
import json
import os
import errno

from string import Template
# RQ01 - Sistemas populares são maduros/antigos?
headers = {"Authorization": ""}


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Error {}. {}".format(request.status_code, query))


query = Template('''
{
  search(query: "stars:>100", type: REPOSITORY, first: 100$after) {
    pageInfo{
        hasNextPage,
        endCursor
    },
    edges {
      node {
        ... on Repository {
          name,
          createdAt,
          nameWithOwner,
          stargazers {
            totalCount
          }
        }
      }
    }
  }
}
''')


filename = "answers/RQ01-answer.json"
if not os.path.exists(os.path.dirname(filename)):
  try:
    os.makedirs(os.path.dirname(filename))
  except OSError as exc:
    if exc.errno != errno.EEXIST:
      raise

page = 0
cursor = ""

while page < 10:
    if page == 0:
        result = run_query(query.substitute(after=''))
    else:
        result = run_query(query.substitute(after=", after: \"%s\"" % cursor))
    print("Result - {}".format(result))
    cursor = result["data"]["search"]["pageInfo"]["endCursor"]
    with open(filename, 'w') as output:
        json.dump(result, output)
    page += 1

print("Written to file RQ01-answer.json")