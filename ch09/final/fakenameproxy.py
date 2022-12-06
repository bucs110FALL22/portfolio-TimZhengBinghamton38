import requests


class Fakenameapi:
    def __init__(self) -> None:
        self.api_url = "https://fakerapi.it/api/v1/persons?_quantity=1"
    
    def get(self):
        """
        Gets the information of a made-up person and retrieves the name
        args: self
        return: request (name)
        """
        request = requests.get(self.api_url)
        request = request.json()
        request = request.get("data")
        self.processed_request = request[0]
        firstname = self.processed_request.get("firstname")
        lastname = self.processed_request.get("lastname")
        name = firstname +" " +lastname
        return name
    
    def get_location(self):
        location_data = self.processed_request.get("address")
        city = location_data.get("city")
        return city