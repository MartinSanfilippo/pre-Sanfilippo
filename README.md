# pre-Sanfilippo, Martin

## Aplicacion creada para registro de clientes, productos y pedidos, ademas permite filtrar datos de los clientes registrados, asi como de los pedidos y de los productos tambien, contiene un login, register y logout. Si no esta registrado la app no permite visualizar las diferentes aplicaciones.

### Pasos para que la aplicacion ande correctamente

1)Clonar el repositorio desde powershell usando git clone  

git clone httpsgithub.comMartinSanfilippopre-SanfilippoMartin.git

2)Luego ir al directorio donde lo clonaste y pararse en la carpeta del repositorio con cd

cd nombre de la carpeta

3)Ejecutar el siguiente comando para que se abra visual studio code 

code .

4)Ejecutar desde la terminal de VS para crear el entorno virtual

python -m venv .venv

5)Luego de ejecutar el entorno virtual, toca activarlo

.venvScriptsactivate

6)Instalamos Django con el siguiente comando 

pip install django

7)Nos vamos a la carpeta project, que esta el archivo manage.py

cd .project

8)Por ultimo ejecutar el siguiente comando 

python manage.py runserver 

9)La aplicacion ya estara en ejecucion en google o su navegador predeterminado.

#### Distintas funciones de la app:

1)En el modulo Clientes: podras crear un cliente nuevo, ver los clientes y buscar tambien.

2)En el modulo Productos: Podras crear un producto nuevo, ver el detalle del mismo, actualizar y borrar, como tambien buscar y filtrar.

3)En el modulo Pedidos: Podras crear nuevos pedidos para los productos que tengan stock, y ver en que estado esta el mismo.

4)En el modulo Profile: Podras actualizar tus datos de perfil, ya sea el nombre de usuario, nombre, apellido y email.