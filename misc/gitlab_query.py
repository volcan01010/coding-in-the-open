# coding: utf-8
from pprint import pprint
import requests

result = requests.get('https://api.github.com/orgs/BritishGeologicalSurvey/repos',
                      params={'per_page': 100, 'type': 'source'})
start_dates = {item['name']: item['created_at'] for item in result.json()}
start_dates = sorted(start_dates.items(), key=lambda x: x[1])
pprint(start_dates)
