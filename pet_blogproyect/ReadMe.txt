Pet Blog Project
Visión del Proyecto
El Pet Blog Project es una aplicación web diseñada para que los dueños de mascotas puedan compartir sus experiencias, inquietudes y conocimientos sobre el cuidado de sus mascotas, en particular de los caninos. La aplicación permite a los usuarios publicar preguntas relacionadas con el cuidado de mascotas, compartir fotos y realizar consultas sobre temas tales como: alimentación, cuidado, comportamiento, anécdotas y otros aspectos importantes del cuidado de sus mascotas. Además, otros usuarios pueden comentar en estas publicaciones para ofrecer su ayuda o compartir experiencias similares.
Propósito
El objetivo principal de este proyecto es proporcionar una solución en línea donde los dueños de mascotas puedan interactuar y compartir información útil sobre el cuidado de sus caninos. La aplicación busca:
•	Facilitar el intercambio de información.
•	Permitir la publicación de preguntas y respuestas sobre el cuidado.
•	Ofrecer una plataforma para compartir fotos de sus mascotas.
•	Facilitar la consulta sobre temas relacionados con la alimentación y el cuidado en general.
Estructura del Proyecto
Modelos
1.	Post: Representa una publicación en el blog, que puede incluir texto, imágenes y metadatos relacionados con el cuidado de mascotas.
2.	Comment: Representa un comentario realizado en una publicación del blog.
3.	Author: Representa al autor de una publicación o comentario en el blog.
Vistas
•	Vistas de Publicaciones: Permiten a los usuarios ver las publicaciones, crear nuevas publicaciones, editar publicaciones existentes y eliminar publicaciones.
•	Vistas de Comentarios: Permiten a los usuarios agregar comentarios a las publicaciones y gestionar sus comentarios.
Serializadores
•	Serializador de Publicaciones: Convierte las instancias de publicaciones en formatos que pueden ser enviados a través del API de forma bidireccional.
•	Serializador de Comentarios: Convierte las instancias de comentarios en formatos que pueden ser enviados a través del API de forma bidireccional.
Configuración
•	settings.py: Contiene la configuración del proyecto Django, incluyendo la configuración de la base de datos (django-apprunner-db), la integración con servicios externos (AWS) y la configuración de la aplicación.
•	urls.py: Define las rutas de la aplicación, conectando las URLs con las vistas correspondientes.
Archivos y Directorios
•	blogapp/: Contiene la lógica principal de la aplicación, incluyendo modelos, vistas, serializadores y archivos de migración.
•	pet_blogproyect/: Contiene la configuración global del proyecto, incluyendo ajustes y rutas.
•	migrations/: Contiene los archivos de migración que permiten la actualización de la base de datos conforme a los cambios en los modelos.

