from flask import Flask # Importa el módulo Flask para crear una aplicación web en Python.
from .models import db # Importa el objeto `db` desde el archivo `models.py`. Este objeto es la instancia de SQLAlchemy que se usará para manejar la base de datos.
from .config import Config # Importa la clase `Config` desde el archivo `config.py`, que contiene la configuración de la base de datos y otras opciones de la aplicación.
from .routes import main # Importa el blueprint `main` desde el archivo `routes.py`, que contiene las rutas de la aplicación.

def configurar_app(): # Definimos una función llamada `configurar_app` que será responsable de crear y configurar la aplicación Flask.
# Crear la instancia de la aplicación Flask
    app = Flask(__name__)
    # Crea una nueva instancia de la aplicación Flask. El argumento `__name__` indica que la instancia se relaciona con el módulo actual.
    # Configuración desde config.py
    app.config.from_object(Config)
    # Carga la configuración de la clase `Config` en `config.py` en la aplicación Flask. Esto incluye la conexión a la base de datos y otras configuraciones.
    app.secret_key = '123'  # Necesario para manejar sesiones y mensajes flash
    # Establece una clave secreta para la aplicación, que es necesaria para manejar sesiones y mensajes flash (notificaciones temporales).
    # Inicializar la base de datos con la aplicación
    db.init_app(app)
    # Inicializa la base de datos en la aplicación Flask. Esto vincula la instancia de la base de datos (`db`) con la aplicación Flask creada.
    with app.app_context():
        db.create_all()
    # Ejecuta las operaciones dentro del contexto de la aplicación Flask. 
    # En este caso, crea todas las tablas en la base de datos definidas en los modelos (si no existen).
    # Registrar el blueprint para manejar las rutas del main
    app.register_blueprint(main)
    # Registra el blueprint `main` en la aplicación. Esto agrega todas las rutas definidas en el blueprint `main` (que está en `routes.py`).
    return app
    # Devuelve la instancia de la aplicación Flask ya configurada y lista para ejecutarse.

