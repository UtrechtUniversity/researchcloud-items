# Role uwsgi
[back to index](../index.md#Roles)

## Summary

Setup a Python webapp using [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/), using Nginx as a reverse proxy. Since this role utilises the [nginx_reverse_proxy](./nginx_reverse_proxy.md) role, the webapp can be easily secured using SRAM authentication.

The uWSGI service translates HTTP requests into UWSGI protocol requests, suitable
for consumption by for instance Python web applications.

The Python application is assumed to be installed already in the location `uwsgi_app_dir`/`uwsgi_app_path`.

## Requires

- Debian-like OS
- Nginx web server (installed via the SRC-Nginx component)

## Description

The playbook can be run in two modes:

1. (Default) Install `uwsgi` and its Python3 plugin via the system package manager (`apt`).
2. Use a pre-existing `uwsgi` installation in a `venv`. To use this mode, set the `uwsgi_venv` variable to the location of venv already containing `uwsgi`.

A `systemd` service named `uwsgi-<uwsgi_app_name>` is created for the application, where `<uwsgi_app_name>` corresponds to the variable documented [below](#variables). You can restart it with e.g. `systemctl restart uwsgi-example`.

Logs for the application will be written to `/var/log/uwsgi/<app_name>.log` and `/var/log/uwsgi/<app_name>_err.log`. Logrotation for these files is activated.

The nginx web server is used as a reverse proxy, using the [reverse_proxy](./nginx_reverse_proxy.md) role. You can configure at which location the application should be served, and if authentication should be used, as per the documentation for that role (see [variables](#variables) below).

## Variables

- `uwsgi_app_dir`: String. Path to the directory where the application to be served by uwsgi should be located (will be created if necessary). Default: `/var/www/uwsgi`.
- `uwsgi_app_path`: String. Path to the Python file within `uwsgi_app_dir`. Default: `app.py`.
- `uwsgi_app_name`: String. Name of the application, to be added to `/etc/uwsgi/apps-available`.
- `uwsgi_plugins`: String. Which uwsgi plugins should be used for this app. Default: `python3`. (See uWSGI documentation.)
- `uwsgi_nginx_mountpoint`: String. The Nginx location specifier determining at which URL the app will be served (for example: `/example/`). Default: `/{{ uwsgi_app_name }}/`.
- `uwsgi_num_workers`: Integer. The number of workers `uwsgi` should spawn to handle requests for this app. Default: 2.
- `uwsgi_venv`: Boolean/String. To use a preexisting installation of `uwsgi` in a venv (rather than using the system-provided `uwsgi`), set this to the path to the root of the `venv`. Default: `false`.
- `uwsgi_proxy_conf`: Dict. Options to be passed to the [reverse proxy role](./nginx_reverse_proxy.md), in addition to the default location and `uwsgi_pass` settings. Example: `{ auth: 'sram' }`. Default: empty.
- `uwsgi_config`: Dict. Key/value pairs that will be translated to `uwsgi` settings added to the application's `.ini` file. Example: `{ callable: 'foobar' }` (see `uwsgi`'s docs for options). Default: empty.
- `uwsgi_config_block`: String. Multiline .ini style key/value pairs to be added to the application's `.ini` file.

## See also

- Role [nginx-reverse_proxy](./nginx_reverse_proxy.md)

## History
2021-2024 Written by Ton Smeele and Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
