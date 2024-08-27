# Real-Time Message Broadcasting Service
This repository contains a real-time message broadcasting service built with FastAPI and WebSockets, designed to run on a Kubernetes cluster managed by Minikube. The service consists of two main components:

**Hello Broadcaster**: A service that broadcasts "Hello world" messages to connected WebSocket clients at random intervals.

**Hello Receiver**: A service that receives and displays these messages in real-time through a web interface.

This is based off of the [Machine Infrastructure HW](./assignment.md). This was built on Windows using WSL Ubuntu 22.04.

## Prerequisites
Before running this service, ensure that you have the following installed:

* [Docker](https://docs.docker.com/get-started/get-docker/): Used for building and running containers.
* [Minikube](https://minikube.sigs.k8s.io/docs/start/): A tool that sets up a local Kubernetes cluster.
* [kubectl](https://kubernetes.io/docs/tasks/tools/): The command-line tool for interacting with Kubernetes clusters.

## Installation and Setup

Execute the provided `run.sh` script to build the Docker images, deploy the services to Minikube, and forward the necessary ports:

```bash
./run.sh
```
## Access the Services: 
After the script completes, you can access the services at the following URLs:

Hello Broadcaster (to view subscribed clients): http://localhost:8000

Hello Receiver (Click "Register" to start receiving messages ): http://localhost:8001




## To-Do List
* Use Helm Charts: Transition to using Helm charts for managing Kubernetes deployments more efficiently.
* Use Kafka for Pub/Sub: Implement Kafka as the pub/sub mechanism to enhance the scalability and reliability of message broadcasting.
* Testing!!: Introduce unit tests, integration tests, and end-to-end tests to ensure the robustness and reliability of the services.
* Error Handling: Introduce proper error and edge case handling to increase stability