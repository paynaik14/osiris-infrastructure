import docker
from docker.errors import APIError, NotFound
import pytest
from unittest import mock

def stopDockerContainer(container_name: str) -> bool:
    client = docker.from_env()
    try:
        container = client.containers.get(container_name)
        container.stop()
        print(f"Container {container_name} stopped successfully.")
        return True
    except NotFound as e:
        print(f"Container not found: {e}")
        return False
    except APIError as e:
        print(f"Failed to stop container: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
#sample input - local test w/ public image and container
#response = stopDockerContainer("my-nginx-container")
#print(response)

#Tests - can be run via command: pytest <program_name>
@pytest.fixture
def mocker():
    with mock.patch('docker.from_env') as _fixture:
        yield _fixture
    
def test_stopDockerContainer_success(mocker):
    mock_client = mocker
    mock_container = mocker.MagicMock()
    mock_client.return_value.containers.get.return_value = mock_container

    result = stopDockerContainer("test-container")
    assert result is True
    mock_client.return_value.containers.get.assert_called_once_with("test-container")
    mock_container.stop.assert_called_once()

def test_stopDockerContainer_not_found(mocker):
    mock_client = mocker
    mock_client.return_value.containers.get.side_effect = NotFound('Container was not found.')

    result = stopDockerContainer("test-container")
    assert result is False

def test_stopDockerContainer_api_error(mocker):
    mock_client = mocker
    mock_client.return_value.containers.get.side_effect = APIError('API Error')

    result = stopDockerContainer("test-container")
    assert result is False

def test_stopDockerContainer_generic_error(mocker):
    mock_client = mocker
    mock_client.return_value.containers.get.side_effect = Exception('An error occurred.')
    
    result = stopDockerContainer("test-container")
    assert result is False
    
