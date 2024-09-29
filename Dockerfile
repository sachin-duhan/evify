# Dockerfile

# Use official Python image as the base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY namiz/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY namiz/ namiz/
COPY main.py .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "main.py"]
