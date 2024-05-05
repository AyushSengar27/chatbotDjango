from django.db import models

class UserPrompt(models.Model):
    username = models.CharField(max_length=100)
    prompt = models.TextField()


class PromptResponse:
    def __init__(self, response):
        self.response = response

class JSONException(Exception):
    def __init__(self, message="JSON parsing error", status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class InternalServerException(Exception):
    def __init__(self, message="Internal server error", status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class NetworkException(Exception):
    def __init__(self, message="Network error", status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)