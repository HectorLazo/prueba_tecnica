# [Prueba Tecnica API][docs]


Prueba Técnica desarrollando una API de usuarios en Python.

## Tabla de contenidos:
---

- [Requerimientos](#requerimientos)
- [Instalación](#instalación)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Endpoints](#endpoints)
- ...[Listar usuarios](#listar-usuarios)
- ...[Crear usuario](#crear-usuario)
- ...[Consultar usuario](#consultar-usuario)
- ...[Editar usuario](#editar-usuario)
- ...[Eliminar usuario](#eliminar-usuario)

---

## Requerimientos

* Python (3.9)
* Django (3.2)
* Django REST Framework (3.13.1)


## Instalación

Clonamos el proyecto desde github a nuestro local... 

    git clone https://github.com/HectorLazo/prueba_tecnica.git nombre_carpeta_destino
    
Instalamos mediante `pip` django y django rest framework cuyas versiones las tenemos en el archivo requirements.txt
    
    python manage.py pip install -r requirements.txt
    
Hacemos las migraciones de nuestro proyecto con los siguientes comandos

    python manage.py makemigrations
    
    python manage.py migrate

Y por último, ejecutamos el servidor...

    python manage.py runserver
    
## Herramientas utilizadas

* [Python](https://www.python.org/) - Lenguaje de programación
* [Django](https://www.djangoproject.com/) - Framework Para Python
* [DjangoRESTFramework](https://www.django-rest-framework.org/) - Framework para crear API REST

## Endpoints


### Listar Usuarios

Lista todos los usuarios creados.

`GET /api/usuario-list/`

#### Response
- **data** - Listado de usuarios

#### Request de ejemplo
`GET /api/usuario-listar/`

#### Example Response
`200 OK`

```javascript
{
  "id": "e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40",
  "nombre": "Juan",
  "apellido": "Astorga",
  "email": "jastorga@gmail.com",
  "fecha_nacimiento": "1980-12-10"
},
{
  "id": "e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c46",
  "nombre": "new Juan",
  "apellido": "new Astorga",
  "email": "newjastorga@gmail.com",
  "fecha_nacimiento": "1980-12-10"
}
```


### Crear Usuario

Si el request es correcto, se crea una instancia 'Usuario'.
El id del usuario es autogenerado en formato UUID, en el retorno aparece el campo creado.

`POST /api/usuario-crear/`

#### Cuerpo

- **nombre** - String que representa el nombre del usuario,
- **appellido** - String que representa el apellido del usuario,
- **email** - String que representa el nombre del usuario en formato correo@mail.com,
- **fecha_nacimiento** - Fecha de nacimiento en formato YYYY-MM-DD,

#### Response
- **usuario** - Usuario con cada uno de sus campos (incluido el id autogenerado que nos servirá para consultar, editar y eliminar el usuario)

#### Errores
- **400** - Causado por un id inválido o porque faltan datos

#### Request de ejemplo
`POST /api/usuario-crear/`

#### Example Response
`200 OK`

```javascript
{
  "id": "e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40",
  "nombre": "new Juan",
  "apellido": "new Astorga",
  "email": "newjastorga@gmail.com",
  "fecha_nacimiento": "1980-12-10"
}
```

### Consultar Usuario

Si el request es correcto, se devuelve una instancia 'Usuario', dados los datos validados.

`GET /api/usuario-detail/{id}/`


#### Parámetros
- **id** - Identificador UUID del usuario

#### Response
- **usuario** - Usuario con cada uno de sus campos

#### Errores
- **400** - Causado por un id inválido.

#### Request de ejemplo
`GET /api/usuario-detail/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`

#### Example Response
`200 OK`

```javascript
{
  "id": "e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40",
  "nombre": "Juan",
  "apellido": "Astorga",
  "email": "jastorga@gmail.com",
  "fecha_nacimiento": "1980-12-10"
}
```

### Editar Usuario

Si el request es correcto, se edita una instancia 'Usuario', dado su id.

`PUT /api/usuario-update/{id}/`
`PATCH /api/usuario-update/{id}/`

#### Parámetros
- **id** - Identificador UUID del usuario

#### Response
- **usuario** - Usuario con cada uno de sus campos

#### Errores
- **400** - Causado por un id inválido o porque faltan datos

#### Request de ejemplo
`PATCH /api/usuario-update/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`

`PUT /api/usuario-update/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`

#### Cuerpo (PATCH)
Con `PATCH` se puede actualizar parcialmente un Usuario
Se puede actualizar uno o varios campos

- **nombre** - nombre nuevo de usuario

#### Cuerpo (PUT)

Con `PUT` se actualizan todos los campos del usuario menos el id (se deben ingresar todos los campos en el cuerpo).

- **nombre** - "new Juan",
- **appellido** - "new Astorga",
- **email** - "newjastorga@gmail.com",
- **fecha_nacimiento** - "1980-12-10",


#### Example Response
`200 OK`

```javascript
{
  "id": "e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40",
  "nombre": "new Juan",
  "apellido": "new Astorga",
  "email": "newjastorga@gmail.com",
  "fecha_nacimiento": "1980-12-10"
}
```


### Eliminar Usuario

Si el request es correcto, se elimina una instancia 'Usuario', dado su id.

`DELETE /api/usuario-delete/{id}/`


#### Parámetros
- **id** - Identificador UUID del usuario

#### Response
- **message** - Mensaje de borrado exitoso.

#### Errores
- **400** - Causado por un id inválido

#### Request de ejemplo
`GET /api/usuario-delete/e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40`


#### Example Response
`200 OK`

```javascript
{
    "message": "El usuario con id e7c88d7d-3cb6-47ff-a8c7-a0fb18bc6c40 se ha eliminado exitosamente"
}
```

