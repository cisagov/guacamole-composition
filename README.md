# guacamole-composition 🥑🐳 #

[![GitHub Build Status](https://github.com/cisagov/guacamole-composition/workflows/build/badge.svg)](https://github.com/cisagov/guacamole-composition/actions)
[![CodeQL](https://github.com/cisagov/guacamole-composition/workflows/CodeQL/badge.svg)](https://github.com/cisagov/guacamole-composition/actions/workflows/codeql-analysis.yml)
[![Known Vulnerabilities](https://snyk.io/test/github/cisagov/guacamole-composition/badge.svg)](https://snyk.io/test/github/cisagov/guacamole-composition)

Creates a Docker composition containing instances of:

- [guacamole](https://hub.docker.com/r/guacamole/guacamole/) clientless
remote desktop gateway.
- [guacd](https://hub.docker.com/r/guacamole/guacd/) server-side proxy for
Guacamole.
- [Postgres](https://hub.docker.com/_/postgres/) relational database.
- [cisagov/guacscanner-docker](https://github.com/cisagov/guacscanner-docker)
  utility for continually scanning the EC2 instances in an AWS VPC and
  updating the Guacamole connections in the underlying PostgreSQL
  database.

## Running ##

A sample [Docker composition](docker-compose.yml) is included
in this repository.

To start the composition, use the command: `docker-compose up`

Connect to the Guacamole web interface at:
[http://localhost/guacamole](http://localhost/guacamole).

The default credentials are `guacadmin`, `guacadmin` - you should change those
as soon as possible.

### Volumes ###

#### postgres ####

| Mount Point | Purpose |
| ----------- | ------- |
| `dbdata` | Stores all database data for the `postgres` container |
| `dbinit` | Stores the `postgres` initialization script for the `guacamole` database resources |

### Ports ###

This composition exposes the following port to the `localhost`:

| Port  | Protocol | Service  | Purpose |
|-------|----------|----------|---------|
| 80    | TCP      | http     | Guacamole web interface |

### Secrets ###

Sample secrets have been provided - you should change these if you use this
composition on a publicly-accessible host:

| Filename | Purpose |
|----------|---------|
| postgres-username | Text file containing the username of the `postgres` user used by the `guacamole` container |
| postgres-password | Text file containing the password of the `postgres` user used by the `guacamole` container |
| private_ssh_key | Text file containing the private SSH key to use for SFTP file transfer in Guacamole. |
| rdp_username | Text file containing the username for Guacamole to use when connecting to an instance via RDP. |
| rdp_password | Text file containing the password for Guacamole to use when connecting to an instance via RDP. |
| vnc_username | Text file containing the username for Guacamole to use when connecting to an instance via VNC. |
| vnc_password | Text file containing the password for Guacamole to use when connecting to an instance via VNC. |
| windows_sftp_base | Text file containing the base path for the SFTP directories that Guacamole will use when connecting to a Windows instance via VNC. |

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
