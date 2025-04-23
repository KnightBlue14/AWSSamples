#!/usr/bin/env python

import requests
import os

x = requests.get('http://localhost:8080/health').json()

if x['scheduler']['status'] == 'healthy':
    print('healthy')
else:
    os.system('source venv/bin/activate')
    os.system('airflow scheduler')