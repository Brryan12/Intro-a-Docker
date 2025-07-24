# 🚀 Introducción a Docker Compose

## 🎥 Mira el video del capítulo

[![Ver en YouTube](https://img.youtube.com/vi/QJmzx5CLJEs/0.jpg)](https://www.youtube.com/watch?v=QJmzx5CLJEs)

## 🤔 ¿Qué es un enfoque Declarativo vs Imperativo?

Cuando trabajamos con automatización, infraestructura como código o contenedores, es importante entender la diferencia entre los enfoques **imperativo** y **declarativo**.

---

### 🔧 Enfoque Imperativo

Vos especificás exactamente **cómo** se deben hacer las cosas. Es más flexible, pero más propenso a errores si se omite algún paso.

**Ejemplo:**
```bash
docker network create mi-red
docker volume create postgres_data
docker run -d --name db --network mi-red -e POSTGRES_USER=admin ...
docker run -d --name backend --network mi-red -e DB_HOST=db ...
```

## 📦 ¿Qué es un enfoque Declarativo?

El enfoque **declarativo** consiste en definir **el estado final deseado** del sistema, y dejar que una herramienta se encargue de ejecutar los pasos necesarios para alcanzar ese estado.

En lugar de decirle al sistema cómo hacer cada paso, simplemente declarás lo que querés lograr.

---

### ✅ Ventajas del enfoque declarativo

- 🔁 Más fácil de mantener
- 📚 Más legible para equipos
- 🧪 Ideal para entornos reproducibles
- 🤖 Compatible con automatización e infraestructura como código

---

**Ejemplo:**

En este ejemplo declarás dos servicios: una base de datos y un backend. No decís cómo crearlos ni en qué orden; solo qué necesitás.

```yaml
version: '3.8'
services:
  db:
    image: postgres
  backend:
    build: ./backend
```

# ¿Qué es un archivo YAML?

Un archivo **YAML** (con extensión `.yaml` o `.yml`) es un archivo de texto que utiliza el formato YAML, un lenguaje de serialización de datos legible para humanos.

---

## Características principales

- **YAML** significa *"YAML Ain't Markup Language"* (YAML no es un lenguaje de marcado).
- Se usa principalmente para **archivos de configuración** y para almacenar datos estructurados.
- Su sintaxis es simple, clara y fácil de leer.
- Utiliza indentación para representar niveles y estructuras de datos (similares a JSON o XML, pero más legible).
- Soporta tipos de datos como listas, diccionarios, valores escalares, entre otros.

---

## Ejemplo básico de archivo YAML

```yaml
persona:
  nombre: Oscar
  edad: 30
  hobbies:
    - programación
    - lectura
    - música
```


## 📦 ¿Qué es Docker Compose?

**Docker Compose** es una herramienta que permite definir y ejecutar múltiples contenedores Docker como una sola aplicación de manera declarativa. Toda la configuración se guarda en un archivo llamado `docker-compose.yml`.

En lugar de ejecutar contenedores manualmente uno por uno de manera imperativa, podés levantar toda una arquitectura con un solo comando:

```bash
docker-compose up -d
```
 y todo lo creado se puede eliminar con el comando:

```bash
docker-compose down
```
### 🎥 Ejemplos en Video

### Ejemplo 1

[![Ejemplo 1](https://img.youtube.com/vi/p5KuC1in8tA/0.jpg)](https://www.youtube.com/watch?v=p5KuC1in8tA)

### Ejemplo 2

[![Ejemplo 2](https://img.youtube.com/vi/_vW2Melc2wk/0.jpg)](https://www.youtube.com/watch?v=_vW2Melc2wk)

### Ejemplo 3

[![Ejemplo 3](https://img.youtube.com/vi/9QV5a8eY-Go/0.jpg)](https://www.youtube.com/watch?v=9QV5a8eY-Go)
