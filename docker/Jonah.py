import docker

###### inspectDockerContainer API
def inspectDockerContainer(container_name: str) -> dict:
    client = docker.from_env()
    #client = docker.DockerClient(base_url='tcp://localhost:2375')
    try:
        container = client.containers.get(container_name)
        container_info = {
            "status": container.status,
            "cpu_usage": get_cpu_usage(container),
            "memory_usage": get_memory_usage(container),
            "ports": format_ports(container.attrs['NetworkSettings']['Ports'])
        }
        return container_info
    except docker.errors.NotFound:
        return {"error": "Container not found"}
    except Exception as exception:
        return {"error": str(exception)}

def format_ports(ports):
    formatted_ports = {}
    if ports:
        for container_port, bindings in ports.items():
            if bindings:
                host_port = bindings[0]['HostPort']
                formatted_ports[host_port] = container_port.split('/')[0]
    return formatted_ports

def get_cpu_usage(container):
    stats = container.stats(stream=False)
    cpu_percentage = (stats['cpu_stats']['cpu_usage']['total_usage'] / stats['cpu_stats']['system_cpu_usage']) * 100
    return f"{cpu_percentage:.2f}%"

def get_memory_usage(container):
    stats = container.stats(stream=False)
    memory_usage = stats['memory_stats']['usage'] / (1024 * 1024)
    return f"{memory_usage:.2f}MB"
###### end of inspectDockerContainer API

###### getDockerLogs API
from datetime import datetime

def getDockerLogs(container_name: str, tail: int = 100) -> list:
    client = docker.from_env()
    #client = docker.DockerClient(base_url='tcp://localhost:2375')
    try:
        container = client.containers.get(container_name)
        logs = container.logs(tail=tail, timestamps=True).decode('utf-8').splitlines()
        formatted_logs = []
        for log in logs:
            timestamp, message = log.split(" ", 1)
            timestamp = timestamp[:-1]
            timestamp = timestamp.split('.')[0]
            dt = datetime.fromisoformat(timestamp)
            formatted_timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
            formatted_logs.append(f"{formatted_timestamp} - {message}")
        return formatted_logs
    except docker.errors.NotFound:
        return [f"Container '{container_name}' not found."]
    except Exception as e:
        return [str(e)]
###### end of getDockerLogs API