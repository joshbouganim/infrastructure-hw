# hello_broadcaster/Dockerfile
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install the dependencies
RUN poetry install --no-root

# Copy the service code
COPY . /app/hello_broadcaster

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the service
CMD ["poetry", "run", "uvicorn", "hello_broadcaster.broadcast_service:app", "--host", "0.0.0.0", "--port", "8000"]
