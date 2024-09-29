# 📝 Namiz API Project

### 🚀 Overview
Namiz is an educational platform API built with **Eve** (REST API framework for MongoDB) and includes functionalities like user management, courses, modules, lectures, quizzes, and certificates. It supports file uploads via **AWS S3** and uses **MongoDB** as the core database.

---

### 🛠️ Features
- **User Management**: Manage students and instructors.
- **Courses & Modules**: Create courses with multiple modules and lectures.
- **Lectures & Quizzes**: Attach lectures and quizzes to each module.
- **Certificates**: Issue certificates upon course completion.
- **File Uploads**: Upload lecture materials to AWS S3.
- **Dockerized Environment**: Easily deploy the API with Docker.

---

### 🔧 Setup Instructions

#### 1. Clone the Repo
```bash
git clone https://github.com/your-repo/namiz.git
cd namiz
```

#### 2. Install Dependencies (with Virtual Environment)
```bash
make install
```

This command will:
- Create a Python virtual environment.
- Install the required dependencies from `requirements.txt`.

#### 3. Run the API
```bash
make run
```

The API will be live at: `http://localhost:5000`.

---

### 🐳 Docker & Docker Compose Setup

#### 1. Build the Docker Image
```bash
make build
```

This builds the Docker image using the `Dockerfile`.

#### 2. Run the Docker Container
```bash
make docker-run
```

This will start the container and run the application on port `5000`.

#### 3. Stop the Docker Container
```bash
make docker-stop
```

#### 4. Remove the Docker Container
```bash
make docker-remove
```

---

### 📦 Docker Compose

We have also included a `docker-compose.yml` file for managing both the API and MongoDB services.

#### To start the services with Docker Compose:
```bash
docker compose -f docker-compose.dev.yaml up
```

This command will:
- Start MongoDB with persistent volume support.
- Run the Namiz API container.

#### To stop the services:
```bash
docker compose -f docker-compose.dev.yaml down
```

---

### 📄 Makefile Commands

- **env**: Creates a Python virtual environment.
- **install**: Installs dependencies in the virtual environment.
- **run**: Activates the virtual environment and runs the app.
- **build**: Builds the Docker image.
- **docker-run**: Runs the Docker container for the app.
- **docker-stop**: Stops the Docker container.
- **docker-remove**: Removes the Docker container.
- **clean**: Cleans up the virtual environment and temporary files.
- **seed**: Seeds the MongoDB database with sample data.
- **test**: Runs tests using `pytest`.

---

### 🧪 Running Tests
```bash
make test
```
This will run all tests with coverage and display verbose output.

