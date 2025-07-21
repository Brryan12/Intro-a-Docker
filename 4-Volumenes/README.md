# 📦 Volúmenes en Docker

## ¿Qué es un volumen?

Un **volumen** en Docker es una forma persistente de almacenar datos generados y utilizados por los contenedores. Los volúmenes existen fuera del ciclo de vida del contenedor, por lo que puedes eliminar el contenedor sin perder los datos. Un volumen al final de cuentas viene siendo un directorio en el que se almacenan datos de un contenedor.

---

## ✅ ¿Por qué usar volúmenes?

- Persistencia de datos (sobrevive aunque se borre el contenedor)
- Compartir datos entre múltiples contenedores
- Mejor rendimiento que los bind mounts (forma de comunicar datos entre local-contenedor)
- Administración sencilla (respaldos, migraciones)

---

## 📂 Comandos básicos para volúmenes en Docker

| Comando                                | Descripción                             |
|----------------------------------------|-----------------------------------------|
| `docker volume create <nombre>`        | Crea un volumen                         |
| `docker volume ls`                     | Lista todos los volúmenes               |
| `docker volume inspect <nombre>`       | Muestra información de un volumen       |
| `docker volume rm <nombre>`            | Elimina un volumen                      |
| `docker volume prune`                  | Elimina volúmenes no utilizados         |


### Ejemplo 1

Crear volumen

```bash
    docker volume create mi-primer-volumen
```

Ver volumenes creados

```bash
    docker volume ls
```

Crear contenedor con el volumen creado

```bash
    docker run -it -v mi-primer-volumen:/volumen ubuntu
```

Creamos un archivo dentro del volumen

```bash
    touch hola.txt
```
Detener y eliminar el primer contenedor

Luego, 

Crear un segundo contenedor con el volumen creado

```bash
    docker run -it -v mi-primer-volumen:/volumen ubuntu
```

### Ejemplo 2

Volumen compartido entre contenedores

Creamos el contenedor 1

```bash
    docker run -it --name contenedor1 -v contenedor1:/volumen ubuntu
```

Creamos el contenedor 2

```bash
    docker run -it --name contenedor2 -v contenedor1:/volumen ubuntu
```

### Ejemplo 3

Enlaces local-contenedor

```bash
    docker run -it -v ./:/volumen ubuntu
```

Ejemplo 4

Copiar archivos de local a contenedor y viceversa

Creamos el contenedor 1

```bash
    docker run -it --name contenedor1 -v contenedor1:/volumen ubuntu
```

Dentro del contenedor creamos un archivo dentro de la carpeta volumen

```bash
    docker touch hola.txt
```

Copiamos el archivo

    ```bash
    docker cp contenedor1:/volumen/hola.txt .
```
