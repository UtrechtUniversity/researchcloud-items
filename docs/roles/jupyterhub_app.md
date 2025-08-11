# Role jupyterhub_app
[back to index](../index.md#Roles)

## Summary

This role installs an application on an existing [JupyterHub](./jupyterhub.md) instance. The application can be either:

- Added to a standard JupyterHub, where the application will appear in JupyterLab and can be launched by the user from there.
- Added as a [standalone application](./jupyterhub_standalone_proxy.md), where JupyterHub directly launches the app (instead of going through JupyterLab).

## Description

- If you want to add an application to a standard JupyterHub (as a JupyterLab extension), you have two options: 
    - Specify a Python package to be installed into the Hub's venv with the `jupyterhub_app_pip` variable (see below).
    - Specify trailets config with the `jupyterhub_app_server_config` variable (see below).
- If you want to add standalone application the the Hub, specify the configuration for a `jupyter-standaloneproxy` app using the `jupyterhub_app_standalone_config` variable. This will be placed into the directory `standalone` inside the directory specified by the `jupyterhub_app_config_dir` variable. See [here](./jupyterhub_standalone_proxy.md#configuration-option-2) for what a standalone config should look like.

## Variables

- `jupyterhub_app_name`: String. Name of the application, used to generate a filename for the standalone config file (if specified). Default: `app`.
- `jupyterhub_app_venv`: String. Path to the JupyterHub instance's `venv`. Default: `/usr/local/jupyterhub`. You can set this to the value `system` to not use a virtual environment.
- `jupyterhub_app_config_dir`: String. Path to the JupyterHub's instance config dir. Default: `/usr/local/etc/jupyter`.
- `jupyterhub_app_pip`: String. Optional. Which package to install into the hub's venv (if set). Default: `""`.
- `jupyterhub_app_standalone_config`: String. Optional. [Trailets configuration for a standalone app](./jupyterhub_standalone_proxy.md#configuration-option-2). Default: `""`.
- `jupyterhub_app_server_config`: String. Optional. [Trailets configuration for a non-standalone proxy server app](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-via-traitlets). Will be added to `jupyter_server_config.py`, automatically loaded `jupyter-serverproxy` extension. **Note**: to allow multiple invocations of this role to add traitlets configuration in this way, see the [example](#jupyterhub_app_server_config).
- `jupyterhub_app_pip_executable`: String. Which command to use to install packages into the venv (can be set to `uv` when it is available). Default: `pip`.

## Example

For more examples, see this role's molecule tests.

### `jupyterhub_app_server_config`

When using the `jupyterhub_app_server_config` parameter, the role will add a block with your specified configuration to the `jupyter_server_config` config file. To support adding multiple applications to the config in this way, make sure that you do not override the settings, but append to it:

```python
### INCORRECT: the below code overwrites previously defined items in c.ServerProxy.servers

c.ServerProxy.servers = {
    "httpd" {
      "command": [
        "/usr/bin/python3",
        "-m",
        "http.server",
        "{port}",
      ]
    }
}

### CORRECT: the below code appends a new item to c.ServerProxy.servers
c.ServerProxy.servers.update({ "httpd": {
  "command": [
    "/usr/bin/python3",
    "-m",
    "http.server",
    "{port}",
  ]
  }
})
```

## See also

- Role [jupyterhub](./jupyterhub.md)
- Role [jupyterhub_standalone_proxy](./jupyterhub_standalone_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
