import docker
from docker.errors import APIError
#username = docker hub username
#password = docker hub password
appImage = "kb546/docker-quickstart"
url = "registry.hub.docker.com"

def pushDockerImage(image_name: str, registry_url: str) -> bool:
    client = docker.from_env()
    try:

        #LOGIN into the account
        client.login(username,password,registry=registry_url)

        #get name of image from docker hub
        image = client.images.get(image_name)

        #push image into the registry
        push_response = client.images.push(image_name, stream=True, decode=True)
        for line in push_response:
            #RESPONSE
            print(line)
        return True

    #ERROR HANDLING
    except APIError as e:
        print(f"Failed to push image: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def pullDockerImage(image_name: str, registry_url:str) -> bool:

    #Docker client instance
    client = docker.from_env()
    try:
        #image reference including registry url
        full_image = f"{registry_url}/{image_name}" if registry_url else image_name

        #Pull image from specified registry
        pull_response = client.images.pull(full_image)

        #PRINTING RESPONSE
        print(f"RESPONSE: {pull_response.tags}")
    
        return True

    except APIError as e:
        print(f"Failed to pull image: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    
     
response = pullDockerImage(appImage,url)
print(response)