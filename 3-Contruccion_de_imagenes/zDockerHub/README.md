# 🐳 Guía: Cómo subir imágenes a Docker Hub

## 🧰 Requisitos previos
- Tener Docker instalado.
- Tener una cuenta en [Docker Hub](https://hub.docker.com).
- Haber creado una imagen Docker local.

---

## 1. Iniciar sesión en Docker Hub

```bash
docker login
```

> Ingresa tu **usuario** y **contraseña** de Docker Hub.  
> Si usas autenticación de dos factores (2FA), utiliza un **token de acceso**.

---

## 2. Etiquetar la imagen

Debes etiquetar tu imagen local incluyendo tu nombre de usuario de Docker Hub:

```bash
docker tag nombre-local-imagen usuarioDockerHub/nombre-repositorio:tag
```

**Ejemplo:**
```bash
docker tag simple-index oscarastua29/simple-index:latest
```

---

## 3. Subir la imagen a Docker Hub

```bash
docker push usuarioDockerHub/nombre-repositorio:tag
```

**Ejemplo:**
```bash
docker push oscarastua29/simple-index:latest
```

---

## 4. Verificar en Docker Hub

- Ve a [hub.docker.com](https://hub.docker.com) e inicia sesión.
- Busca el repositorio:  
  `usuarioDockerHub/nombre-repositorio`
- Verás la imagen y el tag que acabás de subir.

---