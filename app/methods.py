# Importamos funciones de seguridad para manejar contraseñas: 'generate_password_hash' para hashear y 'check_password_hash' para verificar contraseñas.
from werkzeug.security import generate_password_hash, check_password_hash

# Importamos los modelos de base de datos 'db' y 'User' desde el archivo models.py.
from .models import db, User

# Importamos 'flash', que nos permite enviar mensajes de notificación al usuario en la aplicación web.
from flask import flash

# Función para registrar un usuario
def registrar_usuario(name, email, password):
    # Verificar si el usuario ya existe en la base de datos con el mismo email.
    user_exists = User.query.filter_by(email=email).first()
    
    # Si el usuario ya existe, mostramos un mensaje de error usando 'flash' y retornamos False para detener el registro.
    if user_exists:
        flash('El correo ya está registrado. Por favor usa otro correo o inicia sesión.', 'error')
        return False

    # Si el usuario no existe, generamos un hash de la contraseña usando el método pbkdf2:sha256 para mayor seguridad.
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    # Creamos un nuevo objeto 'User' con los datos proporcionados (nombre, email y la contraseña hasheada).
    new_user = User(name=name, email=email, password=hashed_password)

    # Agregamos el nuevo usuario a la sesión de la base de datos.
    db.session.add(new_user)

    # Guardamos los cambios en la base de datos para que el nuevo usuario quede registrado.
    db.session.commit()

    # Mostramos un mensaje de éxito notificando que el registro fue exitoso.
    flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')

    # Retornamos True para indicar que el registro fue completado con éxito.
    return True

# Función para iniciar sesión
def iniciar_sesion(email, password):
    # Buscamos al usuario en la base de datos por su email.
    user = User.query.filter_by(email=email).first()

    # Verificamos si el usuario existe y si la contraseña ingresada coincide con la contraseña hasheada en la base de datos.
    if user and check_password_hash(user.password, password):
        # Si la verificación es exitosa, retornamos el ID del usuario.
        return user.id
    else:
        # Si la verificación falla (usuario no existe o contraseña incorrecta), mostramos un mensaje de error.
        flash('Correo o contraseña incorrectos.', 'error')
        return None  # Retornamos None para indicar que la autenticación falló.
