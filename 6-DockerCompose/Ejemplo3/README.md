### Estructura del ejemplo 3

```text
Ejemplo3/
├── backend/
│ ├── app.py # Código del backend Flask con CORS
│ ├── requirements.txt # Dependencias (Flask, flask-cors)
│ └── Dockerfile # Imagen Docker para backend
├── frontend/
│ └── index.html # Frontend estático servido por Nginx
└── docker-compose.yml # Orquestación de servicios (backend + frontend)
└── README.md
```

## Cómo levantar

Ejecutar:

Utilizará las imagenes ya creadas
```bash
docker-compose up --build -d
```

Reconstruirá las imagenes

```bash
docker-compose up -d
```


## Acceder a:

Frontend: http://localhost:8080

Backend API: http://localhost:5000/api/message


## Cómo bajar y limpiar

Ejecutar:

Eliminación nomral

```bash
docker-compose down
```

Elimina imagenes y contenedores creado

```bash
docker-compose down --rmi all --volumes
```