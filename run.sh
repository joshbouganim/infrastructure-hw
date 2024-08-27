#!/bin/bash

# Exit on any error
set -e

# Start Minikube with specific resources
minikube start --cpus=2 --memory=4096

# Set up the environment to use Minikube's Docker daemon
eval $(minikube -p minikube docker-env)

# Build the Docker images
docker build -t hello-broadcaster:latest ./hello_broadcaster
docker build -t hello-receiver:latest ./hello_receiver

# Deploy the services to Kubernetes
kubectl apply -f k8/hello-broadcaster-deployment.yaml
kubectl apply -f k8/hello-broadcaster-service.yaml
kubectl apply -f k8/hello-receiver-deployment.yaml
kubectl apply -f k8/hello-receiver-service.yaml

# Wait for the services to be up and running
echo "Waiting for services to be up and running..."
sleep 5

# Port forward to localhost for easy access, silence output
kubectl port-forward service/hello-broadcaster-service 8000:8000 > /dev/null 2>&1 &
kubectl port-forward service/hello-receiver-service 8001:8001 > /dev/null 2>&1 &
sleep 1

# Step 8: Provide instructions on how to access the services
echo "Services are up and running!"
echo "You can access the hello-broadcaster service at http://localhost:8000"
echo "You can access the hello-receiver service at http://localhost:8001"
