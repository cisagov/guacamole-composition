"""pytest plugin configuration.

https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-plugins
"""
# Third-Party Libraries
import pytest
from python_on_whales import docker


@pytest.fixture(scope="session")
def guacamole_container(dockerc):
    """Return the guacamole container from the Docker composition."""
    # find the container by name even if it is stopped already
    return dockerc.containers(service_names=["guacamole"], stopped=True)[0]


@pytest.fixture(scope="session")
<<<<<<< HEAD
def guacd_container(dockerc):
    """Return the guacd container from the Docker composition."""
    # find the container by name even if it is stopped already
    return dockerc.containers(service_names=["guacd"], stopped=True)[0]
=======
def dockerc():
    """Start up the Docker composition."""
    docker.compose.up(detach=True)
    yield docker
    docker.compose.down()


@pytest.fixture(scope="session")
def main_container(dockerc):
    """Return the main container from the Docker composition."""
    # find the container by name even if it is stopped already
    return dockerc.compose.ps(services=[MAIN_SERVICE_NAME], all=True)[0]
>>>>>>> a9d6c92ea3ca2760e4a18276d06c668058dd3670


@pytest.fixture(scope="session")
def postgres_container(dockerc):
    """Return the postgres container from the Docker composition."""
    # find the container by name even if it is stopped already
<<<<<<< HEAD
    return dockerc.containers(service_names=["postgres"], stopped=True)[0]
=======
    return dockerc.compose.ps(services=[VERSION_SERVICE_NAME], all=True)[0]
>>>>>>> a9d6c92ea3ca2760e4a18276d06c668058dd3670


def pytest_addoption(parser):
    """Add new commandline options to pytest."""
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modify collected tests based on custom marks and commandline options."""
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
