# Esta parte se encargará de correr el servidor
from app import configurar_app

# Este es el inicializador; se agrega el debug para obtener mensajes de error más detallados
configurar_app().run(debug=True, port=8080)


