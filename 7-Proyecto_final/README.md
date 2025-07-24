# 📝 To-Do List App con Docker Compose

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
├── Respuesta-docker-compose.yml # Orquestador
└── README.md 
```

---

## 🚀 Cómo ejecutar el proyecto

### ✅ Prerrequisitos

Asegúrate de tener instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 🔧 Pasos para correr la app

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/todo-app.git
   cd todo-app
   ```

3. Crea tu archivo docker-compose.yml

2. Ejecuta el comando:
   ```bash
   docker-compose up --build -d
    ```
3. Accede al navgador 

    http://localhost:3000

