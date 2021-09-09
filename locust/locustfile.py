import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")