import requests


class PostsApiPage:
    URL_BASE = "https://jsonplaceholder.typicode.com"
    
    #API_KEY = "your_api_key" 
    
    def get_all_posts(self):
        return requests.get(
            f"{self.URL_BASE}/users" #utilizamos /posts para obtener todos los posts
        )


    def get_one_posts(self,post_id):
        return requests.get(
            f"{self.URL_BASE}/users/{post_id}"
        )

    
    def create_post(self, title, body, user_id): #19:54
        return requests.post(
            f"{self.URL_BASE}/users",
            json={
                "title": title,
                "body": body,
                "userId": user_id
            }
        )
          