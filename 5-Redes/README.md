# REDES EN DOCKER

[![Ver en YouTube](https://img.youtube.com/vi/IQbI91Wb3DA/0.jpg)](https://www.youtube.com/watch?v=IQbI91Wb3DA)

## 🌐 ¿Qué es una red?

Una **red** es un conjunto de dispositivos conectados entre sí para **intercambiar datos**. Estos dispositivos pueden ser computadoras, servidores, teléfonos, contenedores, etc.

---

## 🧠 ¿Para qué sirve una red?

- Compartir archivos y recursos
- Acceder a internet
- Ejecutar aplicaciones distribuidas
- Comunicar procesos o servicios

---

## 🛠️ ¿Qué es una red en Docker?

En Docker, una red es una **infraestructura virtual** que permite que los contenedores:

- Se comuniquen entre sí
- Se conecten con el host
- Accedan a servicios externos (como internet)
- Sean accesibles desde fuera del host (exposición de puertos)

---

## 🌐 Tabla comparativa de tipos de red en Docker

| Tipo de red | ¿Qué es? | ¿Cuándo usarla? | Ventajas | Desventajas |
|-------------|----------|------------------|----------|--------------|
| **bridge**  | Red privada creada por Docker en el host. Contenedores se comunican entre sí por IP interna. | Por defecto en contenedores aislados que necesitan comunicarse entre ellos. | Simple, aislada, configurable con `docker network create`. | No accesible directamente desde otras máquinas. |
| **host**    | El contenedor comparte la pila de red del host (sin NAT). | Alto rendimiento y acceso directo al puerto del host (por ejemplo, servidores, performance). | Bajo overhead, sin NAT. | No hay aislamiento de red, puede haber conflictos de puertos. |
| **overlay** | Red distribuida entre múltiples hosts (requiere Docker Swarm). | Contenedores en diferentes hosts que necesitan comunicarse. | Escalable, ideal para clústeres y microservicios. | Requiere configuración extra (Swarm, cifrado, etc.). |
| **none**    | El contenedor no tiene acceso a ninguna red. | Contenedores totalmente aislados, útiles para pruebas o seguridad extrema. | Total aislamiento. | No tiene acceso a la red ni siquiera al host. |
| **macvlan** | Asigna una dirección MAC única al contenedor (como si fuera un dispositivo en la red). | Cuando querés que el contenedor aparezca como un equipo más en la red física. | IP propia en la red física, ideal para integración con redes legacy. | Configuración más compleja, puede no funcionar bien con WiFi o ciertos switches. |


# 📡 Comandos Básicos para Redes en Docker

A continuación, se presentan comandos esenciales para trabajar con redes en Docker.

| Comando                                               | Descripción                                                                 |
|--------------------------------------------------------|-----------------------------------------------------------------------------|
| `docker network ls`                                   | Lista todas las redes disponibles.                                         |
| `docker network create <nombre>`                      | Crea una nueva red personalizada (por defecto tipo `bridge`).              |
| `docker network create -d <driver> <nombre>`          | Crea una red especificando el driver (bridge, host, overlay, etc.).        |
| `docker network inspect <nombre>`                     | Muestra detalles de la red, como contenedores conectados e IPs.            |
| `docker network rm <nombre>`                          | Elimina una red (debe estar vacía).                                        |
| `docker network connect <red> <contenedor>`           | Conecta un contenedor a una red adicional.                                 |
| `docker network disconnect <red> <contenedor>`        | Desconecta un contenedor de una red.                                       |
| `docker run --network <red> ...`                      | Crea y conecta un contenedor directamente a una red.                       |

> ⚠️ Nota: Si no especificás una red al crear un contenedor, Docker lo conecta automáticamente a la red `bridge` por defecto.


## 🌐 Ejemplos Interactivos de Redes en Docker

### 📘 Ejemplo 1: Nuestra primera red

```bash
# Crear nuestra red
docker network create mi-red

# Crear un contenedor sin especificar la red
docker run -dit --name contenedor-nginx nginx

# Inspeccionar el contenedor
docker inspect contenedor-nginx

# Conectar la red del contenedor
docker network connect mi-red contenedor-nginx

# Inspeccionar el contenedor
docker inspect contenedor-nginx

# Desconectar la red del contenedor
docker network disconnect mi-red contenedor-nginx

```

### 📘 Ejemplo 2: Conectar 2 redes a un contenedor

```bash
# Crear dos redes
docker network create red1
docker network create red2

# Crear contenedor y conectarlo a red1
docker run -dit --name multi-red --network red1 busybox

# Conectar el mismo contenedor también a red2
docker network connect red2 multi-red

# Ver las redes conectadas al contenedor
docker inspect multi-red 
```


### 📘 Ejemplo 3: Crear una red bridge personalizada y conectar dos contenedores

```bash
# Crear red personalizada tipo bridge
docker network create red-ejemplo

# Crear el primer contenedor y conectarlo a la red
docker run -dit --name contenedor1 --network red-ejemplo busybox

# Crear el segundo contenedor y conectarlo a la misma red
docker run -dit --name contenedor2 --network red-ejemplo busybox

# Ingresar al primer contenedor
docker exec -it contenedor1 sh

# Desde dentro del contenedor1, hacer ping al contenedor2 por nombre
ping contenedor2
```

### Ejemplo Extra: Red None

```bash
# Crear un contenedor sin red
docker run -dit --name contenedor-sin-red --network none busybox

# Crear el segundo contenedor y conectarlo a la misma red
docker inspect --name contenedor-sin-red 

```

## Casos útiles para usar la red `none`

### 1. Aislar completamente un contenedor
Si querés ejecutar procesos que **no necesitan acceso a la red** por seguridad o control.

**Ejemplo:** contenedores que ejecutan trabajos de cálculo, procesamiento local o tareas batch sin conexión.

---

### 2. Pruebas de seguridad o desarrollo
Para simular entornos donde no hay red o para probar que tu aplicación funcione sin conexión.

También sirve para verificar qué pasa si falla la red o está bloqueada.

---

### 3. Evitar fugas de datos o accesos no deseados
En entornos donde no querés que el contenedor pueda enviar o recibir datos a través de la red.

---

### 4. Contenedores internos
Procesos auxiliares o *sidecars* que no necesitan red para funcionar, solo interactúan con otros contenedores a través de volúmenes o sockets.

