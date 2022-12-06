import json
import requests

class Iseemtechliterate():
    def __init__(self) -> None:
        self.url = "https://techy-api.vercel.app/api/json"
        funnyquote = requests.get(self.url)
        funnyquote.json()




