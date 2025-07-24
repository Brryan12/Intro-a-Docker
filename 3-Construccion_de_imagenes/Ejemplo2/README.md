# Descripción Ejemplo 2

## 🎥 Mira el video del ejemplo 2

[![Ver en YouTube](https://img.youtube.com/vi/oUBFYVXyrg0/0.jpg)](https://www.youtube.com/watch?v=oUBFYVXyrg0)

Un dockerfile con un poco mas de datos para este ejemplo:

![Dockerfile](Dockerfile)

Donde corremos sobre una imagen de python slim.

Para generar la imagen debemos realizar la construcción del Dockerfile con el siguiente comando

   ```bash
   docker build . -t calculadora
 ```

 Donde:
 
**docker build** es el comando para realizar la construccion de la imagen.

**.** Ruta donde se encuentra el archivo **Dockerfile**, en este caso se encuentra en la misma carpeta donde estamos corriendo el comando, esto lo inidcamos con el **.**

**-t** Flag para indicar cual es el nombre que le queremos colocar a nuestra imagen.

**calculadora** Este va a ser el numbre de nuestra imagen, esto puede variar a gusto.

**Nota:**Revisa que estés dentro de la carpeta para poder ejecutar el comando con la ruta **.** si no tenes que modificarla.

***TIP:***Comando para moverte entre carpetas **cd /<nombre-del-directorio>** dentro de una carpeta / **cd ..** salir de la carpeta actual

Una vez creada la imagen lo podemos comprobar con:

   ```bash
   docker images
 ``` 

Ahora nosotros podemos revisar los parametros y propiedades con los que fue creada esta imagen esto es como "Ver dque hay dentro de nuestra imagen", para ver esto utilizaremos el comando:

   ```bash
   docker inspect calculadora
 ```

Acá podemos encontrar mucha información de esta imagen, entre ellos, los **LABEL** que colocamos, unicamente son visibles de este modo.

Para crear un contenedor a base de esta imagen, usaremos el comando:

   ```bash
   docker run -d -it --name contenedor-calculadora calculadora
 ```

Este contenedor si se ejecuta de manera normal se termina de manera inmediata, esto ya que un contenedor corre siempre y cuando su proceso inicial esté en ejecución, es por eso que se agrega el flag **-it** para que el contenedor se ejecute de manera interactiva

Esto quiere decir que se ha iniciado con una terminal virtual activa que permite al usuario interactuar directamente con el contenedor, como si estuviera dentro de una terminal o consola dentro del mismo.
