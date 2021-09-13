import time
from locust import HttpUser, task, between
import json


with open('/mnt/locust/mock_data.json') as f:
  data = json.load(f)

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    index = 0

    @task(3)
    def post_consumo(self):
        self.client.post("/consumos", json=data[self.index])
        self.index += 1