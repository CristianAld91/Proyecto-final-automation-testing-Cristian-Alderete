from pages.posts_api_page import PostsApiPage
from utils.logger import logger
import pytest_check as check

api = PostsApiPage()

def test_get_one_post():
    logger.info("Test: Get one post")
    
    response = api.get_one_posts(1)
    
    check.equal(
        response.status_code, 
        200, 
        "Status code should be 200"
    )
    body = response.json()
    check.equal(
        body["id"],
        1,
        "Post ID should be 1"
    )
   

def test_posts():
    logger.info("obteniendo todos los posts")
    response = api.get_all_posts()
    check.equal(
        response.status_code, 
        200, 
        "Status incorrecto, se esperaba 200"
    )
    
    posts = response.json()
    check.is_true(
        len(posts) > 0,
        "No se encontraron posts"
    )
    check.is_true(
        isinstance(posts, list),
        "La respuesta no es una lista"
    )


    