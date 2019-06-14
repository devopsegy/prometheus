
from prometheus_client import start_http_server, Metric, REGISTRY , Summary
import random
import requests
import json
import sys
import urllib
import time
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
url = 'https://localhost:4848/monitoring/domain/server/http-service/server/request/processingtime.json'
req = requests.get(url ,verify=False , auth=HTTPBasicAuth('admin', 'admin'))



class JsonCollector(object):
  def __init__(self):
    pass
  def collect(self):
    # Fetch the JSON
    response = json.loads(req.content.decode())
    val = response['extraProperties']['entity']['processingtime']['count']
    # Convert requests to Metric
    metric = Metric('monitoring_data','Processing time','gauge')
    metric.add_sample('processingtime',value=val , labels={})
    yield metric

    val_1 = response['extraProperties']['entity']['processingtime']['starttime']
    metric = Metric('monitoring_data','Average request processing time','gauge')
    metric.add_sample('starttime',value=val_1 , labels={})
    yield metric







if __name__ == '__main__':
  # Server will run at port 8000
  start_http_server(8000)
  REGISTRY.register(JsonCollector())

  while True: time.sleep(1)

