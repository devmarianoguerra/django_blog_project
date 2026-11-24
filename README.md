# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene un proyecto Django con una aplicación llamada `posts`. Permite administrar publicaciones mediante operaciones CRUD y asociar imágenes a los posts.

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto:

```bash
cd NOMBRE_DEL_REPOSITORIO
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## CRUD de posts

Las publicaciones permiten:

- Listar posts publicados.
- Ver el detalle de un post.
- Crear un nuevo post.
- Editar un post existente.
- Eliminar un post mediante una confirmación.

## Imágenes

La aplicación usa Pillow para procesar el campo de imagen del modelo `Post`. Las imágenes se guardan en `media/posts/` y se sirven desde `/media/` durante el desarrollo.

Para probar la carga de imágenes, abrir `/posts/crear/`, completar el formulario y seleccionar un archivo de imagen.

## Aplicaciones

- `posts`: aplicación principal para gestionar las publicaciones del blog.
