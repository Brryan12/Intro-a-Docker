# 🐳 Guía Universal para Instalar Docker en Linux

Valido para la mayoria de distribuciones

## 🔍 Paso 1: Verificar instalación de Docker

```bash
docker --version
```

## 🔍 Paso 2: Instar Docker


Valido para la mayoria de distribuciones

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
## 🔍 Paso 3: Iniciar y habilitar el servicio de Docker

```bash
sudo systemctl start docker
sudo systemctl enable docker
```
