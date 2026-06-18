import requests


class PostsApiPage:
    URL_BASE = "https://jsonplaceholder.typicode.com/posts"
    #API_KEY = "your_api_key" #buscar en clase 12 de api privada
    
    def get_all_posts(self):
        return requests.get(
            f"{self.URL_BASE}/posts"
        )


    def get_one_posts(self,post_id):
        return requests.get(
            f"{self.URL_BASE}/posts/{post_id}"
        )

    
    def create_post(self, title, body, user_id): #19:54
        return requests.post(
            f"{self.URL_BASE}/posts",
            json={
                "title": title,
                "body": body,
                "userId": user_id
            }
        )
    
    def delete_post(self, post_id):
        return requests.delete(
            f"{self.URL_BASE}/posts/{post_id}"
        )        