# 📝 To-Do List App con Docker Compose

## 🎥 Mira el video del Proyecto Final

[![Ver en YouTube](https://img.youtube.com/vi/f1CZvYLkoFU/0.jpg)](https://www.youtube.com/watch?v=f1CZvYLkoFU)

Este es un proyecto fullstack simple que implementa una aplicación de lista de tareas (**To-Do List**) usando:

- ⚙️ **Backend**: Flask (Python)
- 🎨 **Frontend**: React
- 🐳 **Contenedores**: Docker + Docker Compose

...
```text
7-Proyecto_final/
├── backend/ # API Flask
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/ # App React
│ ├── src/
│ │ └── App.js
│ ├── public/
│ ├── package.json
│ └── Dockerfile
├── docker-compose.yml # Por modificar
├── Respuesta-docker-compose.yml # Respuesta/apoyo
└── README.md 
```

---

## 🚀 Cómo ejecutar el proyecto

### ✅ Prerrequisitos

Asegúrate de tener instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

Nota: Si tienes Docker Desktop, por lo general Docker compose se instala automaticamente, para comprobarlo corre en la terminal: 

```bash
 docker-compose -v
 ```

### 🔧 Pasos para correr la app

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/todo-app.git
   cd 7-Proyecto_final
   ```

3. Crea tu archivo docker-compose.yml

2. Ejecuta el comando:
   ```bash
   docker-compose up --build -d
    ```
3. Accede al navgador 

    http://localhost:3000

