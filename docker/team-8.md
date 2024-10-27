## Project 
The goal of this segment is to help manage the Docker containers, images, and related configurations for the Osiris project. 

### Technologies
- Docker
- Python
- [Python SDK](https://docker-py.readthedocs.io/en/stable/) to handle management and API calls
- gRPC for the API framework
- Loguru for logging
- Pytest for testing


## Assignments

### Jason Morales - API Developer

#### Task: `runDockerContainer` API

- **Current Status**:  
  I am in the early learning phase for this API. My goal is to understand Docker container management, Python's interaction with Docker through the `Docker SDK`, and how to expose these functionalities through a FastAPI-based API.

- **Challenges Faced**:  
  1. Learning Docker concepts, specifically how to start containers, set environment variables, and handle port mapping.
  2. Getting familiar with the `Docker SDK for Python` to programmatically interact with Docker.
  3. Understanding how FastAPI can be used to create RESTful endpoints for the Docker management commands.

- **Next Steps**:  
  1. **Learn Docker Basics**:
     - Install Docker locally and set up the Docker CLI.
     - Follow basic tutorials on starting and managing Docker containers using commands like `docker run`, `docker stop`, and `docker ps`.
     - Understand how to specify environment variables (`-e`) and port mapping (`-p`) when starting a container.
   
  2. **Explore Docker SDK for Python**:
     - Install `Docker SDK for Python` using:  
       ```bash
       pip install docker
       ```
     - Read through the [Docker SDK for Python documentation](https://docker-py.readthedocs.io/) to understand how to use commands like `client.containers.run()` to start a container and set options like `ports` and `environment`.
   
  3. **Implement the API Endpoint in FastAPI**:
     - Create a basic FastAPI project following a tutorial or the [FastAPI documentation](https://fastapi.tiangolo.com/).
     - Write a simple route (e.g., `/api/run-container`) and verify it returns a basic response.
     - Use the `Docker SDK for Python` to integrate the `runDockerContainer` functionality within this route.
   
  4. **Testing**:
     - Test running a basic container (like `hello-world`) using the `runDockerContainer` API.
     - Experiment with different environment variables and port mappings to ensure the API parameters work as intended.
     - Implement error handling in the API to manage scenarios like missing images or invalid parameters.

---

#### Task: `stopDockerContainer` API

- **Current Status**:  
  I am in the planning and learning phase for this API. My objective is to understand how to identify and stop running Docker containers using the `Docker SDK` and make this action accessible via a FastAPI route.

- **Challenges Faced**:  
  1. Understanding how to locate a running container by name using the `Docker SDK`.
  2. Learning how to stop a Docker container gracefully and verify its status.
  3. Integrating the stopping functionality into a RESTful API with proper error handling.

- **Next Steps**:  
  1. **Learn How to Stop Docker Containers**:
     - Use Docker CLI commands like `docker stop` to understand the basics of stopping containers.
     - Experiment with stopping containers manually by name or ID and learn how Docker handles container shutdown.
   
  2. **Explore Docker SDK for Stopping Containers**:
     - Use the `Docker SDK for Python` to practice stopping containers. Commands like `client.containers.get('container_name').stop()` will be relevant.
     - Learn how to check container status after stopping to confirm the operation was successful.
   
  3. **Create API Endpoint in FastAPI**:
     - Add a new route to the FastAPI project (e.g., `/api/stop-container`).
     - Implement the stopping functionality within this endpoint using the Docker SDK, ensuring you handle potential errors (e.g., container not found).
   
  4. **Testing**:
     - Write unit tests to validate the `stopDockerContainer` API, ensuring it can stop containers by name.
     - Test edge cases like attempting to stop a non-existent container or stopping a container that has already stopped.
     - Implement error messages that provide clear feedback if stopping the container fails.

---
=======
    

### Ethan Ho - API Developer

#### Task: `buildDockerImage` API

- **Current Status**:
Establishing the gRPC and setting up the foundations for the API calls. Furthermore, looking into the `Docker SDK` and testing it to better understand it. The goal is to implement an API that can generate a Docker Image given a file path to a Docker file, the name of the image, and optional tags. It would return a status boolean. 

- **Challenges Faced**:  
  1. Familiarizing myself with the use of `Docker SDK for Python`.
  2. Understanding how to generate an API using RPC and the gRPC.

- **Next Steps**:  
  1. **Explore Docker's Options and Niches**:
     - Expand my understanding of Docker to make sure we have the desired outputs
   
  2. **Implement the API Endpoint in gRPC**:
     - Set up a Python virtual environment with an RPC and test some Python Docker functionality. 
     - Ensure the gRPC application runs on my computer
     - Begin writing out the API endpoint for `/api/buildDockerImage` to read the Docker file and implement its settings.
     - Ensure the configurations sent by the tags are implemented.
     - Use the `Docker SDK` to implement `buildDockerImage`.
   
  3. **Testing**:
     - Implement a test to ensure the API endpoint has a connection.
     - Implement a test to ensure the API builds a Docker Image.
     - Ensure all configurations are made as requested from the Docker File.
     - Ensure all tags are utilized within the Docker Image.
     - Ensure all edge cases also ensure consistent and proper behavior.
    
#### Task: `removeDockerContainer ` API

- **Current Status**:
Look into the `Docker SDK` and understand how to remove a Docker Container from the system. Implement an API that would take in a container name and return a boolean regarding success.

- **Challenges Faced**:  
  1. Familiarizing myself with the use of `Docker SDK for Python`.
  2. Understanding how to generate an API using gRPC.

- **Next Steps**:  
  1. **Explore Docker's Options and Niches**:
     - Expand my understanding of Docker to make sure we have the desired outputs
   
  2. **Implement the API Endpoint in gRPC**:
     - Set up a Python virtual environment with an RPC and test some Python Docker functionality. 
     - Ensure the gRPC application runs on my computer
     - Begin writing out the API endpoint for `/api/removeDockerContainer` with basic functionality.
     - Use the `Docker SDK` to implement `removeDockerContainer`.
   
  3. **Testing**:
     - Implement a test to ensure the API endpoint has a connection.
     - Implement a test to ensure the API can clean up unneeded containers.
     - Ensure the function provides appropriate responses after running.
     - Ensure all edge cases also ensure consistent and proper behavior.

---

#### Kristian Bulusan - API Developer


#### Task: `PushDockerImage` API
- **Current Status**:  
  I am currently learning about docker images. My objective is to learn the properties of a docker image so that I can use it with the SDK that we are planning to use.

- **Challenges Faced**:  
  1. Understanding how docker image behaves and its properties.
  2. Learning how to use our `Docker SDK`.

- **Next Steps**:  
   1. **Understanding Docker Image Basics**:
     - Understanding its properties like its name and tags
     - Different layers of a docker image
     - Using Docker Image ID's when referencing images
   2. **Ensure Docker is running at least on the local machine**:
     - Have docker installed and behaving properly
  3. **Create API Endpoint in FastAPI**:
     - Add a new route to the FastAPI project (e.g., `/api/stop-container`).
     - Implement the stopping functionality within this endpoint using the Docker SDK, ensuring you handle potential errors (e.g., container not found).
   
  4. **Testing**:
     - Test by building a simple image when using the pushDockerImage function with the proper URL
     - Learn to handle authentication if registry requires it. 
