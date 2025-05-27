# Colabora: Plataforma de Preguntas y Respuestas

Colabora es una plataforma web desarrollada en Flask que permite a los usuarios registrarse, iniciar sesión, publicar consultas (preguntas), y visualizarlas por categorías. Inspirada en sitios como Stack Overflow, Colabora busca fomentar la colaboración en comunidades técnicas.

---

## Tabla de Contenidos

* [Tecnologías utilizadas](#tecnologías-utilizadas)
* [Instalación](#instalación)
* [Ejecución del servidor](#ejecución-del-servidor)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Funcionalidades](#funcionalidades)
* [Capturas de Pantalla](#capturas-de-pantalla)
* [Créditos](#créditos)

---

## Tecnologías utilizadas

* **Python 3.11**
* **Flask** (microframework web)
* **SQLAlchemy** (ORM)
* **PostgreSQL** (base de datos)
* **HTML, CSS** (interfaz de usuario)
* **Jinja2** (motor de plantillas)
* **bcrypt** (hash de contraseñas)
* **Gunicorn** (opcional, para producción)

---

## Instalación

1. Clona este repositorio:

```bash
git clone <URL-del-repositorio>
cd colabora
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura la base de datos en `config.py`. Ya viene predefinida una cadena de conexión a una base en Supabase, pero puedes adaptarla a tu entorno PostgreSQL local.

---

## Ejecución del servidor

Corre la aplicación usando:

```bash
python run.py
```

La app se ejecuta en `http://localhost:8080` por defecto.

---

## Estructura del Proyecto

```
colabora/
├── app/
│   ├── __init__.py         # Configura y crea la app Flask
│   ├── config.py           # Configuración general (base de datos)
│   ├── models.py           # Modelos de base de datos (User, Question, Category)
│   ├── methods.py          # Registro e inicio de sesión
│   ├── routes.py           # Rutas de la app (Blueprint)
│
├── templates/              # Archivos HTML para frontend
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── mis_consultas.html
│   ├── nueva_consulta.html
│   
├── static/                 # Imágenes y recursos estáticos
│   ├── study.jpg
│   
├── run.py                  # Archivo principal para ejecutar el servidor
├── requirements.txt        # Lista de dependencias
```

---

## Funcionalidades

### Autenticación de Usuarios

* Registro de nuevos usuarios
* Inicio y cierre de sesión seguro con hash de contraseñas

### Publicación y Gestíon de Consultas

* Crear nuevas consultas
* Visualizar consultas propias
* Consultas organizadas por categorías

### Interfaz Visual

* Interfaz responsiva con estilos modernos
* Panel de bienvenida con opciones para buscar o crear preguntas

---

## Capturas de Pantalla

Puedes encontrar las plantillas en la carpeta `templates/`. Incluyen vistas modernas como:

* Pantalla de inicio (`index.html`)
* Registro e inicio de sesión (`signup.html`, `login.html`)
* Vista principal con barra de búsqueda (`home.html`)
* Mis consultas y nueva consulta (`mis_consultas.html`, `nueva_consulta.html`)

---

## Créditos

Este proyecto fue desarrollado con fines educativos para aprender Flask, bases de datos relacionales, y el diseño de interfaces web colaborativas.

---

## Licencia

Puedes usar este código con fines educativos y de aprendizaje.

---

**Nota:** No olvides configurar tus variables de entorno sensibles usando un archivo `.env` o actualizando directamente el `config.py` para despliegues en producción.
