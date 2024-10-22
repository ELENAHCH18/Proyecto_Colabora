# Importamos funciones necesarias de Flask y nuestros módulos personalizados.
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .methods import registrar_usuario, iniciar_sesion  # Importamos las funciones de autenticación
from .models import db, User, Question, Category  # Modelos de base de datos

# Crear un blueprint llamado 'main' para gestionar rutas. Un blueprint permite modularizar la aplicación en componentes reutilizables.
main = Blueprint('main', __name__)

# Página de inicio, esta es la ruta principal del sitio web.
@main.route('/')
def index():
    # Si el usuario tiene una sesión activa, se le redirige a la página de inicio autenticado.
    if 'user_id' in session:
        return redirect(url_for('main.home'))
    # Si no hay sesión, se renderiza la página de inicio.
    return render_template('index.html')

# Página de inicio para usuarios autenticados.
@main.route('/home')
def home():
    # Si no hay sesión activa, se muestra un mensaje de advertencia y se redirige al login.
    if 'user_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página.", 'warning')
        return redirect(url_for('main.login'))
    
    # Obtener los datos del usuario autenticado desde la base de datos.
    user = User.query.get(session['user_id'])
    # Renderiza la página principal con la información del usuario.
    return render_template('home.html', user=user)

# Página de mis consultas.
@main.route('/mis_consultas')
def mis_consultas():
    # Si el usuario no ha iniciado sesión, se redirige al login.
    if 'user_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página.", 'warning')
        return redirect(url_for('main.login'))
    
    # Consulta las preguntas (consultas) hechas por el usuario y la categoría de cada una.
    consultas = db.session.query(Question, Category).filter(
        Question.id_user == session['user_id'], 
        Question.id_category == Category.id_category
    ).all()

    # Renderiza la página de "Mis Consultas" pasando las consultas del usuario.
    return render_template('mis_consultas.html', consultas=consultas)

# Página para crear una nueva consulta (formulario GET, procesamiento POST).
@main.route('/nueva_consulta', methods=['GET', 'POST'])
def nueva_consulta():
    # Si se está enviando el formulario (POST).
    if request.method == 'POST':
        # Se obtienen los datos del formulario.
        title = request.form.get('title')
        question_content = request.form.get('question_content')
        id_category = request.form.get('id_category')
        id_user = session['user_id']  # El ID del usuario autenticado.

        # Se crea una nueva consulta con los datos proporcionados y se guarda en la base de datos.
        nueva_consulta = Question(title=title, question_content=question_content, id_category=id_category, id_user=id_user)
        db.session.add(nueva_consulta)
        db.session.commit()

        # Se muestra un mensaje de éxito y se redirige a la página de "Mis Consultas".
        flash("Consulta publicada con éxito.", 'success')
        return redirect(url_for('main.mis_consultas'))

    # Si es un GET, se obtienen todas las categorías disponibles para mostrarlas en el formulario.
    categorias = Category.query.all()
    # Renderiza el formulario para crear una nueva consulta.
    return render_template('nueva_consulta.html', categorias=categorias)

# Página para ver una consulta específica.
@main.route('/consulta/<int:id>')
def ver_consulta(id):
    # Se busca una consulta específica por su ID junto con su categoría.
    consulta = db.session.query(Question, Category).filter(Question.id_question == id, Question.id_category == Category.id_category).first()
    # Renderiza la página que muestra los detalles de la consulta.
    return render_template('ver_consulta.html', consulta=consulta)

# Página de perfil.
@main.route('/perfil')
def perfil():
    # Si no hay sesión activa, se redirige al login.
    if 'user_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página.", 'warning')
        return redirect(url_for('main.login'))
    
    # Se obtiene la información del usuario autenticado.
    user = User.query.get(session['user_id'])
    # Renderiza la página del perfil del usuario.
    return render_template('perfil.html', user=user)

# Registro de usuario (GET muestra el formulario, POST lo procesa).
@main.route('/registro', methods=['GET', 'POST'])
def signup():
    # Si se envía el formulario (POST).
    if request.method == 'POST':
        # Se obtienen los datos del formulario.
        name = request.form.get('nombre')
        email = request.form.get('correo')
        password = request.form.get('password')

        # Se intenta registrar el usuario usando una función personalizada.
        if registrar_usuario(name, email, password):
            # Si el registro es exitoso, se guarda el ID del usuario en la sesión.
            user = User.query.filter_by(email=email).first()
            session['user_id'] = user.id
            # Se redirige a la página de inicio autenticado.
            return redirect(url_for('main.home'))

    # Si es un GET, se muestra el formulario de registro.
    return render_template('signup.html')

# Inicio de sesión (GET muestra el formulario, POST lo procesa).
@main.route('/login', methods=['GET', 'POST'])
def login():
    # Si se envía el formulario (POST).
    if request.method == 'POST':
        # Se obtienen los datos del formulario.
        email = request.form.get('email')
        password = request.form.get('password')

        # Se verifica el inicio de sesión usando una función personalizada.
        user_id = iniciar_sesion(email, password)

        # Si el inicio de sesión es exitoso, se guarda el ID del usuario en la sesión.
        if user_id:
            session['user_id'] = user_id
            # Se redirige a la página de inicio autenticado.
            return redirect(url_for('main.home'))
    
    # Si es un GET, se muestra el formulario de login.
    return render_template('login.html')

# Cerrar sesión.
@main.route('/logout')
def logout():
    # Se elimina la sesión del usuario.
    session.pop('user_id', None)
    # Se muestra un mensaje de éxito y se redirige a la página principal.
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('main.index'))



