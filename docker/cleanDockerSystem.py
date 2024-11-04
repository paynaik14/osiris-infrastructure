import docker
from docker.errors import APIError

def cleanDockerSystem() -> bool:
    client = docker.from_env()
    #checks for unused containers, images, volumes and removes
    try:
        stopped = client.containers.list(all=True, filters={"status": "exited"})
        for container in stopped:
            container.remove()

        images = client.images.list(filters={"dangling": True})
        for image in images:
            client.images.remove(image.id)
        
        volumes = client.volumes.list(filters={"dangling": True})
        for volume in volumes:
            volume.remove()
            
        #true if everything is removed successfully
        return True
    
    #error handling
    except APIError as e:
        print(f"Error cleaning up: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
