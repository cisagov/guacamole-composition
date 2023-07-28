#!/usr/bin/env pytest -vs
"""Tests for Docker composition."""

# Standard Python Libraries
import time

READY_MESSAGES = {
    "guacamole": "Server startup in",
    "guacd": "Listening on host 0.0.0.0",
    "postgres": "database system is ready to accept connections",
}


def test_container_count(dockerc):
    """Verify the test composition and container."""
    # stopped parameter allows non-running containers in results
    assert (
<<<<<<< HEAD
        len(dockerc.containers(stopped=True)) == 5
=======
        len(dockerc.compose.ps(all=True)) == 2
>>>>>>> a9d6c92ea3ca2760e4a18276d06c668058dd3670
    ), "Wrong number of containers were started."


def test_wait_for_ready_guacamole(guacamole_container):
    """Wait for guacamole container to be ready."""
    TIMEOUT = 20
    ready_message = READY_MESSAGES["guacamole"]
    for i in range(TIMEOUT):
<<<<<<< HEAD
        if ready_message in guacamole_container.logs().decode("utf-8"):
=======
        if READY_MESSAGE in main_container.logs():
>>>>>>> a9d6c92ea3ca2760e4a18276d06c668058dd3670
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {TIMEOUT} seconds.'
        )


<<<<<<< HEAD
def test_wait_for_ready_guacd(guacd_container):
    """Wait for guacd container to be ready."""
    TIMEOUT = 10
    ready_message = READY_MESSAGES["guacd"]
    for i in range(TIMEOUT):
        if ready_message in guacd_container.logs().decode("utf-8"):
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {TIMEOUT} seconds.'
        )


def test_wait_for_ready_postgres(postgres_container):
    """Wait for postgres container to be ready."""
    TIMEOUT = 10
    ready_message = READY_MESSAGES["postgres"]
    for i in range(TIMEOUT):
        if ready_message in postgres_container.logs().decode("utf-8"):
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {TIMEOUT} seconds.'
        )
=======
def test_wait_for_exits(dockerc, main_container, version_container):
    """Wait for containers to exit."""
    assert (
        dockerc.wait(main_container.id) == 0
    ), "Container service (main) did not exit cleanly"
    assert (
        dockerc.wait(version_container.id) == 0
    ), "Container service (version) did not exit cleanly"


def test_output(dockerc, main_container):
    """Verify the container had the correct output."""
    # make sure container exited if running test isolated
    dockerc.wait(main_container.id)
    log_output = main_container.logs()
    assert SECRET_QUOTE in log_output, "Secret not found in log output."


@pytest.mark.skipif(
    RELEASE_TAG in [None, ""], reason="this is not a release (RELEASE_TAG not set)"
)
def test_release_version():
    """Verify that release tag version agrees with the module version."""
    pkg_vars = {}
    with open(VERSION_FILE) as f:
        exec(f.read(), pkg_vars)  # nosec
    project_version = pkg_vars["__version__"]
    assert (
        RELEASE_TAG == f"v{project_version}"
    ), "RELEASE_TAG does not match the project version"


def test_log_version(dockerc, version_container):
    """Verify the container outputs the correct version to the logs."""
    # make sure container exited if running test isolated
    dockerc.wait(version_container.id)
    log_output = version_container.logs().strip()
    pkg_vars = {}
    with open(VERSION_FILE) as f:
        exec(f.read(), pkg_vars)  # nosec
    project_version = pkg_vars["__version__"]
    assert (
        log_output == project_version
    ), f"Container version output to log does not match project version file {VERSION_FILE}"


def test_container_version_label_matches(version_container):
    """Verify the container version label is the correct version."""
    pkg_vars = {}
    with open(VERSION_FILE) as f:
        exec(f.read(), pkg_vars)  # nosec
    project_version = pkg_vars["__version__"]
    assert (
        version_container.config.labels["org.opencontainers.image.version"]
        == project_version
    ), "Dockerfile version label does not match project version"
>>>>>>> a9d6c92ea3ca2760e4a18276d06c668058dd3670
