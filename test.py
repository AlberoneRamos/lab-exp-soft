import requests
import json
import os
import errno
# RQ01 - Sistemas populares são maduros/antigos?
headers = {"Authorization": "bearer 7c410c852a4a2d8a07f78b9eb497008971b26c43"}


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Error {}. {}".format(request.status_code, query))

        
query = """
{
  search(query: "stars:>100", type: REPOSITORY, last: 100) {
    edges {
      node {
        ... on Repository {
          name,
          createdAt
          stargazers {
            totalCount
          }
        }
      }
    }
  }
}
"""

result = run_query(query)
print("Result - {}".format(result))
filename = "answers/RQ01-answer.json"
if not os.path.exists(os.path.dirname(filename)):
  try:
    os.makedirs(os.path.dirname(filename))
  except OSError as exc:
    if exc.errno != errno.EEXIST:
      raise

with open(filename, 'w') as output:
  json.dump(result, output)
print("Written to file RQ01-answer.json")