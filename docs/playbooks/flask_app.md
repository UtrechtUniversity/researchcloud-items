# Playbook flask_app
[back to index](../index.md#Roles)

## Summary

Serves an arbitrary Flask app, which runs on localhost using uWSGI, using Nginx as a reverse proxy. The Flask app is installed from a public git repository. The role allows easily enabling authentication for your webapp, using SRAM and Single Sign-On.

## Requires

- Debian-like OS
- Nginx web server (installed via the SRC-Nginx component)

## Description

The user can define:

1. Which Flask app to install, by providing a URL to the appropriate git repo.
2. Which version of Python to use.
3. The location of dependency files, such as `requirements.txt` or `pyproject.toml`, relative to the root of the git repo. These will automatically be installed
4. Whether authentication should be enabled for the webapp.
5. A number of more advanced settings described [below](#variables).

The role installs `uv` to ensure the appropriate Python version for the app is present, and to install the dependencies.

## app.py vs wsgi.py

Serving Flask apps with uWSGI is usually done in one of two major ways:

1. Set the `uWSGI` `wsgi-file` option to the location of `app.py`, which contains a callable `app`.
2. Set the `UWSGI` `module` option to `wsgi:app`, indicating that the file `wsgi.py` in the project contains an `app` callable.

This role will assume the first method is to be used, except when `flask_app_path` is `wsgi.py` -- in that case, it will automatically set the `module` config option to `wsgi:app`.

The user can always modify the `uWSGI` config by setting the `flask_app_uwsgi_config` option (see below).

## Variables

- `flask_app_name`: String. Name of your application.
- `flask_app_repo`: String. Url to a public git repository containing your app.
- `flask_app_version`: String. Git tag or version to use.
- `flask_app_path`: String. Path to the main `.py` file for your Flask app (often `app.py` or `wsgi.py`), relative to the repository root.
- `flask_app_requirements`: String. Comma-separated list of paths to requirements file (.txt or .toml) in the repo.
- `flask_app_env`: String. Environment variables to be added to the environment in which the app is run, e.g. `FOO=bar BAZ=qux`. Default: `''`.
- `flask_app_auth_sram`: Boolean. Whether to enable SRAM authorization / Single-Sign On authentication. Default: true.
- `flask_app_auth_basic`: Boolean. Whether to enable http basic authentication. Default: false. If both this option and `flask_app_auth_sram` are enabled, the latter takes precedence.
- `flask_app_python_version`: String. The version of Python to serve the app with. Default: `3.10`.
- `flask_app_num_workers`: Integer. Number of processes `uWSGI` should spawn to handle requests for the app. Default: `2`.
- `flask_app_uwsgi_config`: String. Additional multiline `.ini` style configuration for `uWSGI`. See `uWSGI` docs for more info, and see the default `.ini` template in the uWSGI role.
- `flask_app_location`: String. Nginx location definition determining which URL to serve the app at. Default: `/`, meaning the app is served at `http://yourworkspacefqdn`. Can also be set to e.g. `/myapp` to serve at `http://yourworkspacefqdn/myapp`.
- `flask_app_username`: String. Optional, used if `flask_app_auth_basic` is enabled to set the username for authentication.
- `flask_app_password`: String. Optional, used if `flask_app_auth_basic` is enabled to set the password for authentication.

## See also

- Role [nginx-reverse_proxy](../roles/nginx_reverse_proxy.md)
- Role [nginx-uwsgi](../roles/nginx_uwsgi.md)
- Role [require_src_nginx](../roles/require_src_nginx.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
