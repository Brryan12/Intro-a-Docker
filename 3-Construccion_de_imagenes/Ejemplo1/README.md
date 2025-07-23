## Descripción Ejemplo 1

Un docker file puede ser un archivo muy simple como el de este ejemplo:

![Dockerfile](Dockerfile)

Donde corremos sobre un ubuntu un simple comando.

Para generar la imagen debemos realizar la construcción del Dockerfile con el siguiente comando

   ```bash
   docker build .  -t primera-imagen
 ```

 Donde:
 
**docker build** es el comando para realizar la construccion de la imagen.

**.** Ruta donde se encuentra el archivo **Dockerfile**, en este caso se encuentra en la misma carpeta donde estamos corriendo el comando, esto lo inidcamos con el **.**

**-t** Flag para indicar cual es el nombre que le queremos colocar a nuestra imagen.

**primera-imagen** Este va a ser el numbre de nuestra imagen, esto puede variar a gusto.

**Nota:** Revisa que estés dentro de la carpeta para poder ejecutar el comando con la ruta **.** si no tenes que modificarla.

**TIP:** Comando para moverte entre carpetas **cd /<nombre-del-directorio>** dentro de una carpeta / **cd ..** salir de la carpeta actual

Una vez creada la imagen lo podemos comprobar con:

   ```bash
   docker images
 ```

Para crear un contenedor a base de esta imagen, usaremos el comando:

   ```bash
   docker run primera-imagen
 ```

 Este contenedor únicamente imprime el mensaje y se termina, esto ya que un contenedor corre siempre y cuando su proceso inicial esté en ejecución

![Ver video Explicativo Ejemplo 1](Ejemplo1.mkv)
