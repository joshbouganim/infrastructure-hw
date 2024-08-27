# hello_receiver/Dockerfile
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
COPY . /app/hello_receiver

# Expose the port that FastAPI will run on
EXPOSE 8001

# Command to run the service
CMD ["poetry", "run", "uvicorn", "hello_receiver.receiver_service:app", "--host", "0.0.0.0", "--port", "8001"]
