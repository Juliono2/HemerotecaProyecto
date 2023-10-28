# HemerotecaProyecto

Este es un proyecto académico desarrollado con Django que incluye las aplicaciones

- `books`: Una aplicación que se encarga de la gestion de informacion propia de los libros
- `users`: Otra aplicación que se encarga de el manejo de datos en los usuarios de la hemeroteca
- `loans`: Una tercera aplicación que se ocupa de los prestamos.

## Requisitos

Asegúrate de tener Python y Django, y complementos de REST instalados en tu entorno de desarrollo.

- [Django] - Framework de alto nivel en Python que fomenta un desarrollo rápido y un diseño limpio y pragmático.
- [Python] - Lenguaje de programacion
- [REST Framework] - Conjunto de herramientas potente y flexible para crear API web.

## Usuario de Prueba
Para entrar a administrador puedes usar este usuario de prueba.

Usuario: juliansanchez
Contraseña: 12345

## Uso
Para ejecutar el servidor de desarrollo de Django y probar el proyecto, utiliza el siguiente comando:
```python manage.py runserver```

Agrega la extension al servidor local generado segun sea la vista que desee contemplar

* localhost:8000/admin/
* localhost:8000/books/
* localhost:8000/users/
* localhost:8000/loans/

para las sub vistas, o vistas especificas añada la vista que quiera consultar.


**Books**
* "books": "http://localhost:8000/books/books/"
* "copy": "http://localhost:8000/books/copy/"
* "publication": "http://localhost:8000/books/publication/"

**Users**
* "authors": "http://localhost:8000/users/authors/"
* "users": "http://localhost:8000/users/users/"
* "suscriptions": "http://localhost:8000/users/suscriptions/"

**Loans**
* "loans": "http://localhost:8000/loans/loans/"

Realizado de esta forma para evitar confusiones entre los modelos frente a las diferentes aplicaciones.


El proyecto realizado cuenta con la configuracion por aplicacion de:

**ViewSet**
**Serializer**
**Urls**

Por ultimo, cuenta con la verificacion en archivo view.py de:

* Crea una suscripcion, que no exista una ya activa para ese usuario.
* Crear un prestamo, que no exista uno activo con la misma copia.

```sh
127.0.0.1:8000
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.) 

   [dill]: <https://github.com/joemccann/dillinger>
   [Django]: <https://www.djangoproject.com/>
   [Python]: <https://www.python.org/>
   [REST Framework]: <https://www.django-rest-framework.org/>
   [Gulp]: <http://gulpjs.com>
