from pages.users_api_page import UsersApiPage
from utils.logger import logger
import pytest_check as check

api = UsersApiPage()

def test_one_users():
    logger.info("Test: Get one user")
    
    response = api.get_one_users(1)#obtenemos el post con id 1
    
    check.equal(
        response.status_code, 
        200, 
        "estatus code incorrecto, se esperaba 200"
    )
    id = response.json()
    check.equal(
        id["id"],
        1,
        "Post ID incorrecto, se esperaba 1"
    )

def test_create_users(users_data):
    
    logger.info("Creando un nuevo post")
    
    response = api.create_users(
        users_data["id"],
        users_data["name"],
        users_data["username"],
        users_data["email"]
    )
    check.equal(
        response.status_code, 
        201, 
        "Estatus code incorrecto, se esperaba 201"
    )
    
def test_delete():#borra id especifico
    logger.info("Borrando user")
    
    api = UsersApiPage()
    
    response = api.delete_users(11)# borra el id creado

    check.equal(response.status_code,200, "El status deberia ser 200")
    check.is_true(response.text == "" or response.json()=={}, "el body deberia estar vacio")
    
    
    