# Importar SQLAlchemy, que es una herramienta para manejar la base de datos relacional de manera ORM (Object-Relational Mapping) en Flask.
from flask_sqlalchemy import SQLAlchemy

# Crear una instancia de SQLAlchemy. Esta instancia será usada para manejar todas las interacciones con la base de datos.
db = SQLAlchemy()

# Definir los modelos que representan las tablas en la base de datos.

# Modelo que representa la tabla 'users' en la base de datos.
class User(db.Model):
    __tablename__ = 'users'  # Define el nombre de la tabla en la base de datos.
    
    # Definimos las columnas de la tabla.
    id = db.Column('id_users', db.Integer, primary_key=True)  # Columna 'id_users', que es la clave primaria (PK) de la tabla 'users'.
    name = db.Column(db.String(50), nullable=False)  # Columna 'name', almacena el nombre del usuario, no puede ser nulo.
    email = db.Column(db.String(100), unique=True, nullable=False)  # Columna 'email', debe ser único y no nulo.
    password = db.Column(db.Text(100), nullable=False)  # Columna 'password', almacena la contraseña del usuario (hash).

# Modelo que representa la tabla 'questions' en la base de datos.
class Question(db.Model):
    __tablename__ = 'questions'  # Define el nombre de la tabla en la base de datos.
    
    # Definimos las columnas de la tabla.
    id_question = db.Column(db.Integer, primary_key=True)  # Columna 'id_question', que es la clave primaria (PK) de la tabla 'questions'.
    title = db.Column(db.String(255), nullable=False)  # Columna 'title', almacena el título de la pregunta, no puede ser nulo.
    question_content = db.Column(db.Text, nullable=False)  # Columna 'question_content', almacena el contenido de la pregunta, no puede ser nulo.
    id_category = db.Column(db.Integer)  # Columna 'id_category', almacena el ID de la categoría a la que pertenece la pregunta.
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_users'), nullable=False)  # Columna 'id_user', que es una clave foránea (FK) referenciando al 'id_users' de la tabla 'users'.
    
    # Definimos una relación con el modelo User. Esto permite acceder a los datos del usuario que hizo la pregunta a través de la relación 'user'.
    user = db.relationship('User', backref='questions')  # 'backref' agrega una referencia inversa, lo que permite que un objeto User acceda a sus preguntas asociadas.

# Modelo que representa la tabla 'category' en la base de datos.
class Category(db.Model):
    __tablename__ = 'category'  # Define el nombre de la tabla en la base de datos.
    
    # Definimos las columnas de la tabla.
    id_category = db.Column(db.Integer, primary_key=True)  # Columna 'id_category', que es la clave primaria (PK) de la tabla 'category'.
    category_name = db.Column(db.String(100), nullable=False)  # Columna 'category_name', almacena el nombre de la categoría, no puede ser nulo.

