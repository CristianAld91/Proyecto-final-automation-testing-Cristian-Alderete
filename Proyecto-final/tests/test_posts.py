from pages.posts_api_page import PostsApiPage
from utils.logger import logger
import pytest_check as check

api = PostsApiPage()

def test_get_one_post():
    logger.info("Test: Get one post")
    
    response = api.get_one_posts(1)#obtenemos el post con id 1
    
    check.equal(
        response.status_code, 
        200, 
        "estatus code incorrecto, se esperaba 200"
    )
    body = response.json()
    check.equal(
        body["id"],
        1,
        "Post ID incorrecto, se esperaba 1"
    )
   

def test_posts():
    logger.info("obteniendo todos los posts")
    response = api.get_all_posts()
    check.equal(#verificamos que el estatus code sea 200
        response.status_code, 
        200, 
        "estatus code incorrecto, se esperaba 200"
    )
    
    posts = response.json()
    check.is_true(#verificamos que se hayan obtenido posts
        len(posts) > 0,
        "No se encontraron posts"
    )
    check.is_true( #verificamos que la respuesta sea una lista
        isinstance(posts, list),
        "La respuesta no es una lista"
    )

def test_create_post(posts_data):
    
    logger.info("Creando un nuevo post")
    
    response = api.create_post(
        posts_data["title"],
        posts_data["body"],
        posts_data["userId"]
    )
    check.equal(
        response.status_code, 
        201, 
        "Estatus code incorrecto, se esperaba 201"
    )
    

