# guacamole-composition #

[![Build Status](https://travis-ci.com/cisagov/guacamole-composition.svg?branch=develop)](https://travis-ci.com/cisagov/guacamole-composition)

Creates a Docker composition containing instances of:

- [guacamole](https://hub.docker.com/r/guacamole/guacamole/) clientless
remote desktop gateway.
- [guacd](https://hub.docker.com/r/guacamole/guacd/) server-side proxy for
Guacamole.
- [nginx](https://hub.docker.com/_/nginx) reverse proxy (to enable HTTPS).
- [Postgres](https://hub.docker.com/_/postgres/) relational database.

## Usage ##

A sample [Docker composition](docker-compose.yml) is included
in this repository.

To start the composition, use the command: `docker-compose up`

Connect to the `guacamole` web interface at:
[https://localhost:8443](https://localhost:8443).
The default credentials are `guacadmin`, `guacadmin` - you should change those
as soon as possible.

### Ports ###

This composition exposes the following port to the localhost:

- [8443](http://localhost:8443): `guacamole web interface`

### Secrets ###

Sample secrets have been provided - you should change these if you use this
composition on a publicly-accessible host:

- `postgres-username`: Text file containing the username of the postgres user
used by the guacamole container
- `postgres-password`: Text file containing the password of the postgres user
used by the guacamole container

### Volumes ###

- postgres
  - `dbdata`: Stores all database data for the postgres container

## Contributing ##

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
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
