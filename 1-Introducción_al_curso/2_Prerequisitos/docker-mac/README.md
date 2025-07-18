# 🐳 Guía para Instalar Docker en macOS (Intel y Apple Silicon)

Docker Desktop para macOS proporciona una forma sencilla de ejecutar contenedores en Mac, sin necesidad de instalar Docker Engine manualmente.

---

## ✅ Requisitos

- macOS 11+ (Big Sur o superior)
- Al menos 4 GB de RAM
- Virtualización habilitada (en Intel) o soporte nativo para Apple Silicon
- [Homebrew](https://brew.sh) instalado (opcional pero recomendado)

---

## 📦 Opción A: Instalar Docker Desktop desde el sitio oficial

1. Ir a [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Seleccionar la versión adecuada:
   - Intel chip (si tu Mac es anterior a 2020)
   - Apple chip (M1/M2/M3)
3. Descargar el `.dmg`
4. Abrir el archivo descargado e instalar Docker como cualquier app de macOS
5. Abrir Docker desde `Aplicaciones`
6. Autorizar permisos si el sistema lo solicita

> Docker Desktop incluye: Docker Engine, Docker CLI, Docker Compose, Kubernetes (opcional), y una interfaz gráfica.

---

## 🛠 Opción B: Instalar con Homebrew

Si preferís usar la terminal:

```bash
brew install --cask docker
