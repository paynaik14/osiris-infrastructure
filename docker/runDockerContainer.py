import docker
import pytest
from docker.errors import APIError
from unittest import mock

def runDockerContainer(image_name: str, container_name: str, ports: dict = None, env_vars: dict = None) -> bool:
    client = docker.from_env()
    try:
        container  = client.containers.run(
            image=image_name,
            name=container_name,
            ports=ports,
            environment=env_vars,
            detach=True
        )
        print(f"Container {container_name} started with ID: {container.id}")
        return True
    except APIError as e:
        print(f"Failed to start container: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

#sample input - local test w/ public image
#response = runDockerContainer("nginx:latest", "my-nginx-container", {"8080": "80"}, {"ENV": "production"})
#print(response)

#Tests - can be run via command: pytest <program_name>
@pytest.fixture
def mocker():
    with mock.patch('docker.from_env') as _fixture:
        yield _fixture

def test_runDockerContainer_success(mocker):
    mock_client = mocker
    mock_container = mocker.MagicMock()
    mock_client.return_value.containers.run.return_value = mock_container

    result = runDockerContainer("test-image:latest", "test-container", {"8080": "80"}, {"ENV": "production"})
    assert result is True
    mock_client.return_value.containers.run.assert_called_once_with(
        image="test-image:latest",
        name="test-container",
        ports={"8080": "80"},
        environment={"ENV": "production"},
        detach=True
    )

def test_runDockerContainer_api_error(mocker):
    mock_client = mocker
    mock_client.return_value.containers.run.side_effect = APIError('API Error')
    
    result = runDockerContainer("test-image:latest", "test-container", {"8080" : "80"}, {"ENV": "production"})
    assert result is False

def test_runDockerContainer_generic_error(mocker):
    mock_client = mocker
    mock_client.return_value.containers.run.side_effect = Exception('An error has occured')

    result = runDockerContainer("test-image:latest", "test-container", {"8080" : "80"}, {"ENV": "production"})
    assert result is False