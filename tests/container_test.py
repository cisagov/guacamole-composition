#!/usr/bin/env pytest -vs
"""Tests for Docker composition."""

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
        len(dockerc.containers(stopped=True)) == 5
    ), "Wrong number of containers were started."


def test_wait_for_ready_guacamole(guacamole_container):
    """Wait for guacamole container to be ready."""
    TIMEOUT = 10
    ready_message = READY_MESSAGES["guacamole"]
    for i in range(TIMEOUT):
        if ready_message in guacamole_container.logs().decode("utf-8"):
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {TIMEOUT} seconds.'
        )


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
