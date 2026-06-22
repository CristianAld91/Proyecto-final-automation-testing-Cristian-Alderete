import requests


class UsersApiPage:
    URL_BASE = "https://jsonplaceholder.typicode.com"
    
    #API_KEY = "your_api_key" 


    def get_one_users(self,id):
        return requests.get(
            f"{self.URL_BASE}/users/{id}"
        )

    
    def create_users(self, id,name,username,email): #19:54
        return requests.post(
            f"{self.URL_BASE}/users",
            json={
                "id": id,
                "name": name,
                "username": username,
                "email": email
            }
    
        )
    
    def delete_users(self, user_id):
        return requests.delete(
            f"{self.URL_BASE}/users/{user_id}"
        )