# Proyecto final 
### Cursada: Automatización QA

### Autor: Cristian Alderete

### Profesor: Brayann Farfan
### Tutora: Amancay Arribillaga

## Tecnologías utilizadas
- **Python 3.13**
- **pytest** como framework de pruebas
- **pytest-check** para validaciones múltiples sin detener la ejecución
- **requests** para realizar llamadas HTTP
- **logging** para registrar la ejecución de pruebas

## Funcionalidades implementadas
### PostsApiPage
- `get_all_posts()` → obtiene todos los posts.
- `get_one_posts(post_id)` → obtiene un post específico.
- `create_post(title, body, user_id)` → crea un nuevo post.

### UsersApiPage
- `get_one_users(id)` → obtiene un usuario específico.
- `create_users(id, name, username, email)` → crea un nuevo usuario.
- `delete_users(user_id)` → elimina un usuario por ID.

## Pruebas incluidas
- **Posts**
  - Obtener un post por ID y validar el `status_code` y el `id`.
  - Obtener todos los posts y verificar que la respuesta sea una lista con elementos.
  - Crear un nuevo post y validar que el `status_code` sea `201`.

- **Users**
  - Obtener un usuario por ID y validar el `status_code` y el `id`.
  - Crear un nuevo usuario y validar que el `status_code` sea `201`.
  - Eliminar un usuario y verificar que el body esté vacío.

## Ejecución de pruebas
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
