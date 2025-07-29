# Role jupyterhub
[back to index](../index.md#Roles)

## Summary

Install [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/) on the workspace, by default with SRAM auth enabled.

## Requires

- Debian-family OS (tested on Ubuntu >= 22)
- SURF's [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component preinstalled

## Description

This role installs the JupyterHub webapplication.

The role will set the `jupyterhub_venv_path` fact to the path of the virtual environment containing JupyterHub, for other roles or playbooks to use.

### Authentication and authorization

This role utilizes the [nginx_reverse_proxy](./nginx_reverse_proxy.md) to activate support for Single Sing-on using SRAM (via the `jhub_remote_user_authenticator` [plugin](https://github.com/cwaldbieser/jhub_remote_user_authenticator)). If SRAM auth is enabled, extra Python code is added to the JupyterHub config file to enable use of `jhub_remote_user_authenticator`.

SRAM authentication is default, but can also be disabled. Other options include no authentication, or http basic auth.

JupyterHub's [sudospawner](https://github.com/jupyterhub/sudospawner) is used to run notebooks as specific users: when you login with user `foo` (usin e.g. SRAM), the hub (which runs as a dedicated service user itself) will use special `sudo` permissions to spawn a notebook server running as user `foo` on the workspace. Only users in the group specified by `jupyterhub_allowed_users_group` variable are allowed to spawn in this way.

**Note**: at the moment JupyterHub listens on a TCP port (8000). This means users with shell access can easily bypass authentication. **Do not provide shell access to untrusted users**. In the future we may remedy this by using Docker containers or unix sockets.

## Variables

- `jupyterhub_port`: Int. Port on which the hub will listen. Default: `8000`.
- `jupyterhub_uri`: String. Base URL under which the Hub will be served. Default: `/`.
- `jupyterhub_auth`: String. Should be one of `sram`, `basic`, or `noauth`. See the [nginx location role](./nginx_location.md). Default: `sram`.
- `jupyterhub_bind_addr`: String. IP address/host on which the hub will be listening. Default: `127.0.0.1`.
- `jupyterhub_extra_pkgs`: List. Extra pypi packages that will be installed in jupyterhub's `venv` in addition the required base packages. Default: `[]`.
- `jupyterhub_config_extra`: String. Extra python code that will be inserted in the JupyterHub config file. The config object is called `c`. See the [JupyterHub docs](https://jupyterhub.readthedocs.io/en/5.2.1/reference/api/app.html). Default: `""`.
- `jupyterhub_allowed_users_group`: String. Name of the group, users in which will be able to use `jupyterhub`.
- `jupyterhub_enable_notebooks`: Boolean. Whether to actually enable the use of notebooks. This can be disabled for non-standard use of JupyterHub, e.g. with the [standalone proxy](./jupyterhub_standalone_proxy.md). Default: `true`.
- `jupyterhub_config_env_keep`: List of environment variables, the values of which will be passed along to each spawned webapplication. Default: `['JUPYTERHUB_ACTIVITY_URL', 'JUPYTERHUB_SERVER_NAME', 'PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'JUPYTERHUB_SINGLEUSER_APP']`.
- `jupyterhub_proxy_config`: Dict. Settings that will be passed on to the `nginx_reverse_proxy` role. Will be merged with the default proxy settings, so this variable allows you to override settings. See the [proxy role](./nginx_reverse_proxy.md) for what the dict should look like. Default: `{}`.
- `jupyterhub_http_username`: String. HTTP username to use when setting `jupyterhub_auth` to `basic`. Default: `""`.
- `jupyterhub_http_password`: String. Default:: `""`.
- `jupyterhub_create_default_group`: Boolean. Default: `true`.
- `jupyterhub_remote_user_header`: String. Which HTTP header should be used to get the username from, when using remote user auth (SRAM). Default: `REMOTE_USER`.
- `jupyterhub_activate_remote_user_auth`: Boolean. Whether to enable remote user auth in the JupyterHub config. You can set this to `true` in order to test remote auth without actually having SRAM or another external auth provider, e.g. in CI. Default: `false`.

## See also

- Role [nginx_reverse_proxy](./nginx_reverse_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
