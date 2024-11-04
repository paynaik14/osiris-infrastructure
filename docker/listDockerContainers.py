import docker

def listDockerContainers() -> list:
    client = docker.from_env()
    try:
        #retrieve list of all containers
        containers = client.containers.list(all=True)
        cont = []
        #checks if at least one container exists
        if not containers:
            return "No containers found."
        else:
            for container in containers:
                #checks image tag for error handling
                try:
                    image = container.image.tags[0] if container.image.tags else "no tag"
                except docker.errors.ImageNotFound:
                    image = "image not found"
                #{"name": "my-app-container", "image": "my-app-image:latest", "status": "running"}
                cont.append(
                    {
                        "name": container.name,
                        "image": image,
                        "status": container.status
                    }
                )
            return cont
    
    #error handling
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
