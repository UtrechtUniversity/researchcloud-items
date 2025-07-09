# Playbook flask_app
[back to index](../index.md#Roles)

## Summary

Serves an arbitrary Flask app, which runs on localhost using uWSGI, using Nginx as a reverse proxy. The Flask app is installed from a public git repository. The role allows easily enabling authentication for your webapp, using SRAM and Single Sign-On.

1. From a public git repo
1. From PyPi (specifying package name and version)
1. From a requirements file on the target machine. The main advantages of this mode is that it allows you to specify specific dependencies, and that by committing a requirements file to your playbook's repo, you can use something like Dependabot to keep updating to the latest available version of your app.
    * **Note**: *when using this mode, you must still set the `flask_app_pip_pkg` variable to the name of the package that contains your app, so the role knows which of the dependencies in the requirements file is the app you want to run!*

## Requires

- Debian-like OS
- Nginx web server (installed via the SRC-Nginx component)

## Description

The user can define:

1. Which Flask app to install, by providing a URL to the appropriate git repo (`flask_app_repo`), or by setting a PyPi package to install (`flask_app_pip_pkg`).
2. Which version of Python to use.
3. The location of dependency files, such as `requirements.txt` or `pyproject.toml`, relative to the root of the git repo. These will automatically be installed
4. Whether authentication should be enabled for the webapp.
5. A number of more advanced settings described [below](#variables).

## Variables

See the [role documentation](../roles/flask_app.md) for variables that you can set in this playbook, **but note** that the parameters are called differently: where the *role* parameter is called, e.g. `flask_app_pip_pkg`, the parameter for this playbook is called `flask_pip_pkg`.

**Note**: while individual uWSGI settings have their own variable, you can always use `flask_uwsgi_config_block` to add arbitary settings:

* `flask_uwsgi_config_block`: String. Pass in arbitary `key = value` settings with explicit newlines, e.g. `foo = bar\nbar = foo`.

## See also

- Role [flask_app](../roles/flask_app.md)
- Role [nginx_reverse_proxy](../roles/nginx_reverse_proxy.md)
- Role [nginx_uwsgi](../roles/nginx_uwsgi.md)
- Role [require_src_nginx](../roles/require_src_nginx.md)

## History
2024-2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
