# coding: utf-8
import requests

result = requests.get('https://api.github.com/orgs/BritishGeologicalSurvey/repos',
                      params={'per_page': 100, 'type': 'forks'})
start_dates = {item['name']: item['created_at'] for item in result.json()}
print(start_dates)
