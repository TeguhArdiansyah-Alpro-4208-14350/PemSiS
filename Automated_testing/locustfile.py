from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.client.post("/api/v1/auth/sign-in", json={"username": "user", "password": "pass123!"})

    @task
    def login(self):
        self.client.post("/api/v1/auth/sign-in", json={"username": "user", "password": "pass123!"})
