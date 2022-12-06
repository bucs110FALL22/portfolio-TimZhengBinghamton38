import requests

class Techyquoteapi:
    def __init__(self) -> None:
        self.api_url = "https://techy-api.vercel.app/api/json"
    
    def get(self):
        """
        Gets the techy sounding quote and processes it into a string
        args: self 
        return: response (a string with the quote)
        """
        request = requests.get(self.api_url)
        response = request.json()
        response = str(response)
        response = response[13:len(response)-2]
        return response
