# FastAPI Learning Project

## 1. Setting up the Environment with Docker

To create and use the Python environment with Docker, execute the following command at the root of the project:

```
docker-compose up -d --build
```

To stop and remove containers, networks, volumes, and all images associated with the services defined in Docker Compose:

```
docker compose down --rmi all -v
```

---

## 2. How to Run the FastAPI Project

To run the FastAPI project locally, use the following command in your terminal, inside the project folder:

```
uvicorn app:app --host 0.0.0.0 --port 4000 --reload
```

- `uvicorn` is a fast and lightweight ASGI (Asynchronous Server Gateway Interface) server, used to run asynchronous Python applications. It allows your application to respond to multiple requests simultaneously, leveraging asynchronous programming capabilities for improved performance and scalability. Uvicorn is commonly used in both development and production environments to serve modern APIs written in Python.
- `app:app` indicates the Python file and the FastAPI application instance.
- `--host 0.0.0.0 --port 4000` defines the server's address and port.
- `--reload` enables automatic reloading mode during development.
- The service will be available at [http://localhost:4000](http://localhost:4000).

---