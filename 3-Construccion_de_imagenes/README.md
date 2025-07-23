
# ¿Qué es un Dockerfile?

Un **Dockerfile** es un archivo de texto que contiene una serie de instrucciones para construir una imagen de Docker. Estas instrucciones definen el sistema operativo base, las aplicaciones que se instalarán, los archivos que se copiarán y el comando que se ejecutará al iniciar un contenedor a partir de esa imagen.

---

## Características principales

- Se escribe en un lenguaje declarativo específico para Docker.
- Permite automatizar la creación de imágenes.
- Facilita la reproducibilidad y portabilidad de aplicaciones.
- Es utilizado por el comando `docker build` para construir imágenes.

---


## 🧱 Comandos base del Dockerfile

| Comando     | Descripción                                                                 |
|-------------|------------------------------------------------------------------------------|
| `FROM`      | Especifica la **imagen base**. Debe ser la primera línea válida del Dockerfile. |
| `RUN`       | Ejecuta comandos en una **capa intermedia** durante la construcción de la imagen. |
| `CMD`       | Define el **comando por defecto** que se ejecutará al iniciar el contenedor. |
| `LABEL`     | Añade **metadatos** a la imagen en forma de pares clave/valor.              |
| `EXPOSE`    | Documenta los **puertos** que el contenedor escuchará en tiempo de ejecución. |
| `ENV`       | Define **variables de entorno** que estarán disponibles dentro del contenedor. |
| `ADD`       | Copia archivos/directorios al contenedor y **descomprime automáticamente** archivos `.tar`. |
| `COPY`      | Copia archivos/directorios **sin descomprimir** desde el contexto al contenedor. |
| `ENTRYPOINT`| Establece el **comando principal** que no se sobrescribe fácilmente.        |
| `VOLUME`    | Declara un volumen para **almacenar datos persistentes**.                  |
| `WORKDIR`   | Establece el **directorio de trabajo** dentro del contenedor.              |
| `USER`      | Define el **usuario** que ejecutará los comandos dentro del contenedor.    |
| `ARG`       | Declara **variables de construcción** (solo disponibles durante el `docker build`). |
| `ONBUILD`   | Especifica comandos que se ejecutarán cuando la imagen sea usada como base. |
| `SHELL`     | Cambia el **intérprete por defecto** usado en los comandos `RUN`, `CMD`, etc. |
