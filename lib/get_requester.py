import requests
import json  # Import the json module

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Fetch the response from the URL
        response = requests.get(self.url)
        # Return the raw response content
        return response.content

    def load_json(self):
        # Fetch the response body
        response_body = self.get_response_body()
        # Parse and return the JSON data
        return json.loads(response_body)  # Use json.loads to parse the raw bytes
