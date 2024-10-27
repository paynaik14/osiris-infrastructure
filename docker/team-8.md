# Assignments

## Jason Morales - API Developer

### Task: `runDockerContainer` API

**Current Status:**

I am in the early learning phase for the `runDockerContainer` API. My goal is to understand Docker container management, Python's interaction with Docker through the Docker SDK, and how to expose these functionalities through a **gRPC-based API** within the **Osiris** platform.

**Challenges Faced:**

- **Understanding Docker Concepts:** Learning how to start containers, set environment variables, and handle port mapping effectively.
- **Docker SDK for Python:** Getting familiar with the Docker SDK for Python to programmatically interact with Docker.
- **Implementing gRPC Services:** Transitioning from RESTful APIs to gRPC services, including defining Protocol Buffer messages and service methods.

**Next Steps:**

1. **Learn Docker Basics:**
   - **Install Docker Locally:** Set up Docker on the development machine and familiarize myself with the Docker CLI.
   - **Basic Tutorials:** Follow tutorials on starting and managing Docker containers using commands like `docker run`, `docker stop`, and `docker ps`. Understand how to specify environment variables (`-e`) and port mapping (`-p`) when starting a container.

2. **Explore Docker SDK for Python:**
   - **Install Docker SDK:**
     ```bash
     pip install docker
     ```
   - **Read Documentation:** Study the [Docker SDK for Python documentation](https://docker-py.readthedocs.io/en/stable/) to understand how to use methods like `client.containers.run()` to start a container and set options like ports and environment variables.

3. **Define gRPC Service for `runDockerContainer`:**
   - **Update Protocol Buffers:** Define the `RunDockerContainer` RPC method with appropriate request and response messages in the `docker_management.proto` file.

4. **Implement the `DockerService` Server:**
   - **Implement the `RunDockerContainer` Method:** Develop the server-side logic for handling the `RunDockerContainer` RPC method using the Docker SDK.
   - **Containerize the DockerService Server:** Create a Docker image for the `DockerService` server to ensure consistent deployment across environments.

5. **Testing:**
   - **Test Running a Basic Container:** Use the `RunDockerContainer` API to start a simple container (e.g., `hello-world`) and verify its execution.
   - **Experiment with Parameters:** Test different environment variables and port mappings to ensure the API parameters work as intended.
   - **Error Handling:** Implement and test error handling scenarios, such as attempting to start a container with a missing image or invalid parameters.

### Task: `stopDockerContainer` API

**Current Status:**

I am in the planning and learning phase for this API. My objective is to understand how to identify and stop running Docker containers using the Docker SDK and make this action accessible via a **gRPC-based API** within the **Osiris** platform.

**Challenges Faced:**

- **Locating Running Containers:** Understanding how to locate a running container by name using the Docker SDK.
- **Graceful Shutdown:** Learning how to stop a Docker container gracefully and verify its status.
- **Implementing gRPC Services:** Integrating the stopping functionality into a gRPC service with proper error handling.

**Next Steps:**

1. **Learn How to Stop Docker Containers:**
   - **Docker CLI Commands:** Use Docker CLI commands like `docker stop` to understand the basics of stopping containers.
   - **Manual Stopping:** Experiment with stopping containers manually by name or ID and observe how Docker handles container shutdown.

2. **Explore Docker SDK for Stopping Containers:**
   - **Stopping Containers:** Use the Docker SDK for Python to practice stopping containers programmatically.
   - **Check Container Status:** Learn how to check the container's status after stopping to confirm the operation was successful.

3. **Implement the gRPC Service Endpoint for `stopDockerContainer`:**
   - **Define RPC Methods:** Define the `StopDockerContainer` RPC method in the `docker_management.proto` file.
   - **Implement Server Logic:** Develop the server-side logic to handle stopping Docker containers using the Docker SDK.

4. **Testing:**
   - **Unit Tests:** Write unit tests to validate the `stopDockerContainer` API, ensuring it can stop containers by name.
   - **Edge Cases:** Test scenarios like attempting to stop a non-existent container or stopping a container that has already stopped.
   - **Error Messages:** Implement and test error messages that provide clear feedback if stopping the container fails, such as "Container not found" or "Container already stopped."

---
