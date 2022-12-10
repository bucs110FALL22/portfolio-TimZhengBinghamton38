import requests

class Randquoteapi:
    def __init__(self) -> None:
        self.api_url = "https://api.quotable.io/random"
    
    def get(self):
        """
        Gets the quote and its author/"attributed to person" and processes it into a string
        args: self 
        return: author , quote
        """
        request = requests.get(self.api_url)
        response = request.json()
        author = response.get('author')
        quote = response.get('content')
        return author, quote

    def __str__(self) -> str:
        return self.api_url
