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
    # all parameter allows non-running containers in results
    assert (
        len(dockerc.compose.ps(all=True)) == 4
    ), "Wrong number of containers were started."


def test_wait_for_ready_guacamole(guacamole_container):
    """Wait for guacamole container to be ready."""
    timeout = 20
    ready_message = READY_MESSAGES["guacamole"]
    for _i in range(timeout):
        if ready_message in guacamole_container.logs():
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {timeout} seconds.'
        )


def test_wait_for_ready_guacd(guacd_container):
    """Wait for guacd container to be ready."""
    timeout = 10
    ready_message = READY_MESSAGES["guacd"]
    for _i in range(timeout):
        if ready_message in guacd_container.logs():
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {timeout} seconds.'
        )


def test_wait_for_ready_postgres(postgres_container):
    """Wait for postgres container to be ready."""
    timeout = 10
    ready_message = READY_MESSAGES["postgres"]
    for _i in range(timeout):
        if ready_message in postgres_container.logs():
            break
        time.sleep(1)
    else:
        raise Exception(
            f"Container does not seem ready.  "
            f'Expected "{ready_message}" in the log within {timeout} seconds.'
        )


def test_initialized_postgres(postgres_container, postgres_username):
    """Check that the PostgreSQL database has been initialized for Guacamole."""
    # Here we're assuming that if PostgreSQL contains a
    # guacamole_connection table within the guacamole_db database then
    # it is fully initialized.
    response = postgres_container.execute(
        [
            "psql",
            "--dbname=guacamole_db",
            "--command=\\dt",
            f"--username={postgres_username}",
        ]
    )
    assert "guacamole_connection" in response
