# Role jupyterhub_standalone_proxy
[back to index](../index.md#Roles)

## Summary

Use JupyterHub's proxy to spawn and serve an arbitrary webapplication (instead of a Jupyter Notebook), running as any user that logs in to the hub. This allows you to e.g. serve an IDE running as user `foo` when `foo` logs in, and an IDE running as user `bar` when `bar` logs in.

This role uses the [JupyterHub role](./jupyterhub.md), so it supports SRAM authentication.

The role uses the [`jupyter-server-proxy` standalone plugin](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html), so that instead of getting the Hub webpage and having to select a web application, users are immediately served the desired webapplication after logging in.

## Requires

- Debian-family OS (tested on Ubuntu >= 22)
- SURF's [SRC-Nginx](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) component preinstalled

## Description

This role levarages JupyterHub's proxy to spawn and serve an arbitrary webapplication (instead of a Jupyter Notebook), running as a specific user. To see how you can determine which application should be spawned, see [the examples](#examples).

The role uses the [JupyterHub role](./jupyterhub.md), so it supports SRAM authentication. It modifies the JupyterHub to replace the default command that is spawned by the Hub: instead of running a notebook server, the [jupyter-standalone-proxy](https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html) command will be executed (via the `sudospawner` command), with the config file provided.

JupyterHub's [sudospawner](https://github.com/jupyterhub/sudospawner) is used to run the desired webapp as a specific user: when you login with user `foo` (usin e.g. SRAM), the hub (which runs as a dedicated service user itself) will use special `sudo` permissions to spawn the webapp running as user `foo` on the workspace.

Only users in the group specified by `jupyterhub_allowed_users_group` variable are allowed to spawn in this way.

## Variables

- `jhsp_extra_pkgs`: List. Extra pypi packages that will be installed in jupyterhub's `venv` in addition the required base packages. Default: `[]`.
- `jhsp_standalone_proxy_config_file`: String. Path to the config file for `jupyter-standalone-proxy`. Default: `/etc/jupyterhub/standalone-proxy-config.py`.
- `jhsp_standalone_proxy_config`:  String. Contents of the config file for `jupyter-standalone-proxy`.  Default: `""`.
- `jhsp_standalone_proxy_cmd`: String. The command that will be spawned when a user logs in. Default: `"jupyter-standaloneproxy"`.
- `jhsp_standalone_proxy_cmd_args`: List of command line args provided to `jhsp_standalone_proxy_cmd`. Default: `["--config={{ jhsp_standalone_proxy_config_file }}"]`.
- `jhsp_config_env_keep`: List of environment variables, the values of which will be passed along to each spawned webapplication. Default: `['JUPYTERHUB_ACTIVITY_URL', 'JUPYTERHUB_SERVER_NAME', 'PATH', 'PYTHONPATH', 'JUPYTERHUB_SINGLEUSER_APP']`.
- `jhsp_jupyterhub_user`: String. The user the hub itself should run as. Default: `jupyter`.
- `jhsp_jupyterhub_allowed_users_group`: String. Name of the group, users in which will be able to use the hub.

## Examples

To determine which command will be spawned when a user logs in, you can either:

1. Let  `jhsp_standalone_proxy_cmd_args` be the default. This will make `jupyter-standalone-proxy` use the config file (in the location specified by `jhsp_standalone_proxy_config_file`), with the contents you specify in `jhsp_standalone_proxy_config`. See [below](#example-using-a-config-file).
2. Alternatively, you can override `jhsp_standalone_proxy_cmd_args`. This way you can tell `jupyter-standalone-proxy` to ignore the config file, and instead directly invoke a specific command. In this case, you would use the role as follows. See [below](#example-overriding-jhsp_standalone_proxy_cmd_args).

Remember that you can override variables for the [jupyterhub role](./jupyterhub.md) in your playbook. For example, to disable authentication, you could:

```yaml
- name: Test
  hosts: all
  gather_facts: true
  vars:
    jupyterhub_auth: noauth
  roles:
    - role: jupyterhub_standalone_proxy
      # your vars here
```

### Example: using a config file

```yaml
- role: jupyterhub_standalone_proxy
    vars:
    jhsp_standalone_proxy_config: |
        # Example of a config file for jupyter standaloneproxy
        # See https://jupyter-server-proxy.readthedocs.io/en/latest/standalone.html
        # Specify the command to execute
        c.StandaloneProxyServer.command = [
            "voila", "--no-browser", "--port={port}", "/path/to/some/Notebook.ipynb"
        ]

        # Specify address and port
        c.StandaloneProxyServer.address = "localhost"
        c.StandaloneProxyServer.port = 8000

        # Disable authentication
        c.StandaloneProxyServer.no_authentication = True
```

#### Example: overriding `jhsp_standalone_proxy_cmd_args`

```yaml
- role: jupyterhub_standalone_proxy
    vars:
    jhsp_standalone_proxy_cmd_args:
        - "--" # after this comes the command to be run as a specific logged-in user
        - "/usr/bin/python3"
        - "-m"
        - "http.server"
        - "{unix_socket}" # special argument that the standalone proxy will replace with the location fo the unix socket for the specific user.
```

The above example will spawn the default python webserver for each user, running in their own home directory.

## See also

- Role [jupyterhub](./jupyterhub.md)
- Role [nginx_reverse_proxy](./nginx_reverse_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
