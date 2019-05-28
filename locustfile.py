from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def agenda(self):
        self.client.get("/agenda")

    @task(3)
    def questionAnswer(self):
        self.client.get("/view")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
