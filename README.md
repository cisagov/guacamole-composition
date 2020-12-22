# guacamole-composition 🥑🐳 #

[![GitHub Build Status](https://github.com/cisagov/guacamole-composition/workflows/build/badge.svg)](https://github.com/cisagov/guacamole-composition/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/guacamole-composition.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/guacamole-composition/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/guacamole-composition.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/guacamole-composition/context:python)

Creates a Docker composition containing instances of:

- [guacamole](https://hub.docker.com/r/guacamole/guacamole/) clientless
remote desktop gateway.
- [guacd](https://hub.docker.com/r/guacamole/guacd/) server-side proxy for
Guacamole.
- [Postgres](https://hub.docker.com/_/postgres/) relational database.

## Nota bene ##

We currently use [a custom version of the Guacamole Docker
image](https://hub.docker.com/r/cisagov/guacamole) mentioned above.
This is because the official Guacamole Docker image does not include
[the `guacamole-auth-header-*.jar` file that is required to provide
header-based
authentication](https://guacamole.apache.org/doc/gug/header-auth.html).
We use header-based authentication in order to leverage our Kerberos
setup via an Apache web proxy.  This functionality will be added to
the official Guacamole Docker image in Docker Hub with the next
release of Guacamole, at which time we can revert to using the
official Docker image.  See
[apache/guacamole-client#548](https://github.com/apache/guacamole-client/pull/548)
for more details.

## Usage ##

A sample [Docker composition](docker-compose.yml) is included
in this repository.

To start the composition, use the command: `docker-compose up`

Connect to the `guacamole` web interface at:
[http://localhost/guacamole](http://localhost/guacamole).

The default credentials are `guacadmin`, `guacadmin` - you should change those
as soon as possible.

### Ports ###

This composition exposes the following port to the `localhost`:

| Port  | Protocol | Service  | Purpose |
|-------|----------|----------|---------|
| 80    | TCP      | http     | `guacamole` web interface |

### Secrets ###

Sample secrets have been provided - you should change these if you use this
composition on a publicly-accessible host:

| Filename | Purpose |
|----------|---------|
| postgres-username | Text file containing the username of the postgres user
used by the guacamole container |
| postgres-password | Text file containing the password of the postgres user
used by the guacamole container |

### Volumes ###

- postgres
  - `dbdata`: Stores all database data for the postgres container
  - `dbinit`: Stores the postgres initialization script for the guacamole
  database resources

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
