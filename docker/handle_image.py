import docker 
from loguru import logger
client = docker.from_env()

def buildDockerImage(dockerfile_path: str, image_name: str, tags: list = None) -> bool:
    """build a docker image that takes in the tags and generates the image"""
    if tags is None:
        tags = []
    
    logger.info(f"Building docker image: {image_name} with tags: {tags} from path: {dockerfile_path}")

    try: 
        image, logs = client.images.build(path=".", dockerfile=dockerfile_path, rm=True)
        for tag in tags:
            image.tag(image_name, tag=tag)
        logger.info(logs)
        logger.success(f"Built docker image: {image_name} with tag: {tag}")
        return True
    except Exception as e:
        logger.error(f"Error building docker image: {e}")
        return False
    

def removeDockerContainer(container_name: str) -> bool:
    """remove a docker container"""

    try: 
        container = client.containers.get(container_name)
        container.stop()
        container.remove()
        logger.success(f"Removed docker container: {container_name}")
        return True
    except Exception as e:
        logger.error(f"Error removing docker container: {e}")
        return False

    pass
