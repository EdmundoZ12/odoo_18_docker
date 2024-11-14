![VAMOSSSS!](https://i.pinimg.com/564x/f0/40/9d/f0409d15cd71bbf81d83526e87efb231.jpg "Gato chingon")

# Odoo 18 con docker
### Requisitos windows
* Tener instalado docker desktop

### Pasos
1. Duplicar y renombrar: 
    * Duplicar .env.copy y renombrar la copia con el nombre .env .
    * Duplicar odoo.conf.copy y renombrar la copia con el nombre odoo.conf.

    Es importante no editar ni renombrar los archivos que contengan el nombre la palabra copy, ya que estos forman parte de tu plantilla.
2. Establece los parámetros de tu instancia en el archivo .env
    * Solo editar WEB_PORT, WEBSOCKET_PORT, DB_PORT si es necesario

3. Establece los parámetros de tu instancia en el archivo config/odoo.conf
    * los parámetros DB_HOST,DB_PASSWD y DB_USER, se establecen en .env. Estos tambien se configuran en el archivo odoo.conf 
    * Si estas en producción el parámetro ADMIN_PASSWD de odoo.conf debe ser uno seguro, ya que con este parámetro se gestionan las base de datos.

4. Ejecución con docker-compose
En la misma raiz del proyecto donde se encuentra docker-compose.yaml, debes ejecutar:
    * La primera vez descargará las imagenes de odoo y postgres, esto puede demorar varios minutos.
    * Las siguientes ejecuciones deberá demorar solo segundos para iniciarse.

    ~~~~
    docker-compose up -d
    ~~~~

5. Ingresa a Odoo
    * El parámetro WEB_PORT lo definiste en el archivo .env
    * Ingresa a localhost:<WEB_PORT>
    * Siendo la primera vez que ingresas al sistema, el sistema te mostrará un formulario para que puedas crear una base de datos.

### CREDITOS

Ottoniel Campos
https://github.com/hutzon
https://www.youtube.com/@programacionbluehat
