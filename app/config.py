class Config:  
    # Definimos una clase llamada 'Config' que actuará como la configuración general para la aplicación.

    # Crear la cadena de conexión a PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.vcniilsfhfgbqwphqtdo:YaelSUPA1387#@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    # Definimos 'SQLALCHEMY_DATABASE_URI', que es la cadena de conexión que SQLAlchemy utilizará para conectarse a una base de datos PostgreSQL.
    # La cadena tiene el siguiente formato: 'postgresql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_base_de_datos>'
    # Aquí, 'postgres.vcniilsfhfgbqwphqtdo' es el nombre de usuario, 'YaelSUPA1387#' es la contraseña,
    # 'aws-0-us-west-1.pooler.supabase.com' es el host donde está alojada la base de datos,
    # '6543' es el puerto, y 'postgres' es el nombre de la base de datos.

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Esta configuración desactiva la característica de seguimiento de modificaciones de SQLAlchemy. 
    # Al establecer este valor como 'False', evitamos el uso innecesario de recursos ya que no queremos que SQLAlchemy rastree todos los cambios en los objetos.
