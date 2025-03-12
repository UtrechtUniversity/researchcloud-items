# Role flask_app
[back to index](../index.md#Playbooks)

## Summary

Serves an arbitrary Flask app, which runs on localhost using uWSGI, using Nginx as a reverse proxy. The Flask app is installed either from a public git repository, or from PyPi. The role allows easily enabling authentication for your webapp, using SRAM and Single Sign-On.

The role allows installing the app in the different ways:

1. From a public git repo
1. From PyPi (specifying package name and version)
1. From a requirements file on the target machine. The main advantages of this mode is that it allows you to specify specific dependencies, and that by committing a requirements file to your playbook's repo, you can use something like Dependabot to keep updating to the latest available version of your app.
    * **Note**: *when using this mode, you must still set the `flask_app_pip_pkg` variable to the name of the package that contains your app, so the role knows which of the dependencies in the requirements file is the app you want to run!*

## Requires

- Debian-like OS
- Nginx web server (installed via the SRC-Nginx component)

## Description

The user can define:

1. Which Flask app to install, by either:
  * setting a URL to the appropriate git repo.
  * setting a PyPi package name
2. Which version of Python to use.
3. The location of dependency files, such as `requirements.txt` or `pyproject.toml`, relative to the root of the git repo. These will automatically be installed
4. Whether authentication should be enabled for the webapp.
5. A number of more advanced settings described [below](#variables).

The role installs `uv` to ensure the appropriate Python version for the app is present, and to install the dependencies.

## app.py vs wsgi.py

Serving Flask apps with uWSGI is usually done in one of two major ways:

1. Set the `uWSGI` `wsgi-file` option to the location of `app.py`, which contains a callable `app`.
2. Set the `UWSGI` `module` option to `wsgi:app`, indicating that the file `wsgi.py` in the project contains an `app` callable.

This role will assume the first method is to be used, except when `flask_app_module_path` is `wsgi.py` -- in that case, it will automatically set the `module` config option to `wsgi:app`.

The user can always modify the `uWSGI` config by setting the `flask_app_uwsgi_config` option (see below).

## Variables

Many of the variables below are to configure the uWSGI settings. While individual settings have their own variable, note that you can always use either `flask_app_uwsgi_config` (pass in a dict) or `flask_app_uwsgi_config_block` (pass in a string) to configure arbitrary settings.

- `flask_app_name`: String. Name of your application. This is descriptive: it determines, for instance, the directory under which files will be saved (e.g. `/var/www/myappname`). Default: `FlaskApp`.
- `flask_app_pip_pkg`: String. Name of the PyPi package that contains the app. You must set *either* this variable, *or* `flask_app_repo` (but not both).
- `flask_app_repo`: String. Url to a public git repository containing your app. You must set *either* this variable, *or* `flask_app_pip_pkg` (but not both).
- `flask_app_version`: String. Git tag or version to use.
- `flask_app_module_path`: String. Path to the main `.py` file for your Flask app (often `app.py` or `wsgi.py`), relative to the repository root.
- `flask_app_pip_requirements`: String. Comma-separated list of paths to requirements file (.txt or .toml), the contents of which will be installed in the venv. When using `flask_app_pip_pkg`, this will be assumed to be a file on the target machine. When using `flask_app_repo`, it will be assumed to be a path inside the specified repository.
- `flask_app_uwsgi_env`: String. Environment variables to be added to the environment in which the app is run, e.g. `FOO=bar BAZ=qux`. Default: `''`.
- `flask_app_python_version`: String. The version of Python to serve the app with. Default: `3.10`.
- `flask_app_num_workers`: Integer. Number of processes `uWSGI` should spawn to handle requests for the app. Default: `2`.
- `flask_app_uwsgi_config`: Dict. Settings to be added to the `uWSGI` `.ini` config file, according to `key=value`.
- `flask_app_uwsgi_config_block`: String. Additional multiline `.ini` style configuration for `uWSGI`. See `uWSGI` docs for more info, and see the default `.ini` template in the uWSGI role.
- `flask_app_chdir`: Boolean. If `true`, the app will be executed from the directory containing the app's code.
- `flask_app_proxy_auth`: String. Set to `sram` to enable SRAM authorization / Single-Sign On authentication, `basic` for HTTP basic auth, or omit for no authentication. Default: `sram`.
- `flask_app_proxy_location`: String. Nginx location definition determining which URL to serve the app at. Default: `/`, meaning the app is served at `http://yourworkspacefqdn`. Can also be set to e.g. `/myapp` to serve at `http://yourworkspacefqdn/myapp`.
- `flask_app_http_username`: String. Optional, used if `flask_app_proxy_auth_basic` is enabled to set the username for authentication.
- `flask_app_http_password`: String. Optional, used if `flask_app_proxy_auth_basic` is enabled to set the password for authentication.

## See also

- Playbook [flask_app](../playbooks/flask_app.md)
- Role [nginx_reverse_proxy](../roles/nginx_reverse_proxy.md)
- Role [nginx_uwsgi](../roles/nginx_uwsgi.md)
- Role [require_src_nginx](../roles/require_src_nginx.md)

## History
2024-2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
