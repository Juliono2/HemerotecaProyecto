# HemerotecaProyecto

Este es un proyecto académico desarrollado con Django que incluye las aplicaciones

- `books`: Una aplicación que se encarga de la gestion de informacion propia de los libros
- `users`: Otra aplicación que se encarga de el manejo de datos en los usuarios de la hemeroteca
- `loans`: Una tercera aplicación que se ocupa de los prestamos.
- `locations`: Una cuarta aplicación que se encarga de la logica para el almacenamiento de libros

## Requisitos

Asegúrate de tener Python y Django, y complementos de REST instalados en tu entorno de desarrollo.

- [Django] - Framework de alto nivel en Python que fomenta un desarrollo rápido y un diseño limpio y pragmático.
- [Python] - Lenguaje de programacion
- [REST Framework] - Conjunto de herramientas potente y flexible para crear API web.
- [Simple JSON Web Token] - Proporciona un backend de autenticación de token web JSON para Django REST Framework
- [Swagger Documentation] - Genera la documentación de los endpoints junto con todos metodos.

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
* localhost:8000/locations/
* localhost:8000/api/token
* localhost:8000/api/token/refresh
* localhost:8000/swagger/
* localhost:8000/redoc/

para las sub vistas, o vistas especificas añada la vista que quiera consultar.


**Books**
* "books": "http://localhost:8000/books/books/"
* "copy": "http://localhost:8000/books/copy/"
* "publication": "http://localhost:8000/books/publication/"

**Users**
* "sign-up": "http://localhost:8000/users/sign-up"
* "authors": "http://localhost:8000/users/authors/"
* "suscriptions": "http://localhost:8000/users/suscriptions/"

**Loans**
* "loans": "http://localhost:8000/loans/loans/"
* "lateloans": "http://localhost:8000/loans/lateloans/"
* "debts": "http://localhost:8000/loans/debts/"

**Locations**
* "booklocations": "http://localhost:8000/locations/book-location/"
* "sections": "http://localhost:8000/locations/section/"
* "shelf": "http://localhost:8000/locations/shelf/"

Realizado de esta forma para evitar confusiones entre los modelos frente a las diferentes aplicaciones.

## Nota aclaratoria
**_El proyecto cuenta con asignacion de roles, por lo tanto algunas acciones van a estar limitadas, adicionalmente cuenta con una autentificacion usando tokens, por lo tanto debera de agregarse el token realizar las acciones a las acciones dentro de la request._**

Utilice el end-point "sign-up": "http://localhost:8000/users/sign-up", para registrarse con el rol que desee, (esta accion deberia de solo poderla realizar el administrador pero esta definido asi para facilitar revision)

Los roles de usuario son:
| # |Rol| Descripcion|
|----|----|--|
|1. |Biblotecario | Usuario encargado de realizar los prestamos. |
|2. |Catalogador | Usuario encargado unicamente de modificar aspectos de ubicacion, sin embargo, no tiene permitido crear. |
|3. |Lector | Usuario con un rol por defecto, sus permisos solo le permiten leer.|
|4. |Administrador | Usuario con mayor poder dentro de la hemeroteca, puede hacer de todo. |

El proyecto realizado cuenta con la configuracion por aplicacion de:

| Concepto | Descripción |
| ------ | ------ |
| **ViewSet** | Clase en Django REST framework que combina funcionalidades de vistas y enrutamiento, simplificando la creación de API CRUD. |
| **Serializer** | Herramienta que convierte los modelos de Django en datos JSON para su uso en APIs, facilitando la representación y validación de datos. |
| **Urls** | Definiciones de patrones de URL que mapean las vistas de una aplicación web o API, permitiendo la navegación y acceso a recursos específicos. |
| **Permission**  | Define los permisos a los cuales podra acceder cada usuario segun sus roles asignados |

Por ultimo, cuenta con la verificacion en archivos view.py segun la aplicacion de:

* Asignacion de permisos segun el rol del usurio
* Crea una suscripcion, que no exista una ya activa para ese usuario.
* Crear un prestamo, que no exista uno activo con la misma copia.
* Generar prestamos retardados y deuda segun el update del estado del prestamo y su fecha de final del prestamo, para ello cambie el estado de un prestamo a inactivo, y si su fecha de entrega es menor a la fecha actual, se generar una deuda.

Considere la siguiente ruta, el ".../loans/2" indica el segundo prestamo, cambie su dicho numero segun el prestamo al cual cambiara de activo a inactivo. 
```sh
http://localhost:8000/loans/loans/2/
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.) 

   [dill]: <https://github.com/joemccann/dillinger>
   [Django]: <https://www.djangoproject.com/>
   [Python]: <https://www.python.org/>
   [REST Framework]: <https://www.django-rest-framework.org/>
   [Gulp]: <http://gulpjs.com>
   [Swagger Documentation]: <https://drf-yasg.readthedocs.io/en/stable/readme.html#usage>
   [Simple JSON Web Token]: <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/>