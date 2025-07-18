## 🛠️ Comandos esenciales

| Comando                           | Descripción                                  |
|-----------------------------------|----------------------------------------------|
| `docker run hello-world`          | Ejecuta una imagen de prueba                 |
| `docker ps`                       | Lista contenedores en ejecución              |
| `docker ps -a`                    | Lista todos los contenedores                 |
| `docker stop <nombre/id>`         | Detiene un contenedor                        |
| `docker start <nombre/id>`        | Inicia un contenedor detenido                |
| `docker rm <nombre/id>`           | Elimina un contenedor                        |
| `docker rmi <nombre/id>`          | Elimina una imagen                           |
| `docker logs <nombre/id>`         | Muestra los logs del contenedor              |
| `docker exec -it <nombre/id> bash`| Ejecuta comandos dentro del contenedor       |

---
![Ver video contenedores esenciales](contenedores_esenciales.mkv)

### Nota: Cuando se quiere detener/iniciar/eliminar un contenedor o imagen, se puede hacer mediante el comando respectivo y el ID o el nombre

Ejemplo: 

En el caso del contenedor de tetris, se podia detener de cualquiera de las siguientes maneras:

1. Container ID:
   ```bash
   docker stop 2b28ab0022d

2. Name:
   ```bash
   docker stop juego_tetris


## 💡 Ejercicio 1: Tu primer contenedor

1. Ejecutá el clásico `hello-world`:
   ```bash
   docker run hello-world


## 💡 Ejercicio 2: Corriendo contenedores

Crea un contenedor con la imagen nginx

   ```bash
   docker run -d nginx
 ```
Deten el contenedor

   ```bash
   docker stop <container id>
 ```
Inicia el contenedor

   ```bash
   docker start <container id>
 ```
Elimina el contenedor

   ```bash
   docker rm <container id>
 ```

 Elimina la imagen de nginx

    ```bash
   docker rmi nginx
 ```


## 💡 Ejercicio 3: Jugando con contenedores


Descarga la imagen de tetris 

    ```bash
   docker pull bsord/tetris
 ```

 Crea un contenedor partiendo de esa imagen y despliegalo en el puerto 80

    ```bash
   docker run -d -p 80:80 --name tetris bsord/tetris
 ```
 Mira los logs del contenedor

   ```bash
   docker logs <container id>
 ```

 Navega dentro del contenedor 
 
   ```bash
   docker exec -it <container id> bash
 ```