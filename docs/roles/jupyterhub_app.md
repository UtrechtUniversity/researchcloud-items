# Role jupyterhub_app
[back to index](../index.md#Roles)

## Summary

This role installs an application on an existing [JupyterHub](./jupyterhub.md) instance. The application can be either:

- Added to a standard JupyterHub, where the application will appear in JupyterLab and can be launched by the user from there.
- Added as a [standalone application](./jupyterhub_standalone_proxy.md), where JupyterHub directly launches the app (instead of going through JupyterLab).

## Description

- If you want to add an application to a standard JupyterHub (as a JupyterLab extension), you'll have to specify a Python package to be installed into the Hub's venv with the `jupyterhub_app_pip` variable.
- If you want to add standalone application the the Hub, specify the configuration for a `jupyter-standaloneproxy` app using the `jupyterhub_app_standalone_config` variable. This will be placed into the directory `standalone` inside the directory specified by the `jupyterhub_app_config_dir` variable. See [here](./jupyterhub_standalone_proxy.md#configuration-option-2) for what a standalone config should look like.

## Variables

- `jupyterhub_app_name`: String. Name of the application, used to generate a filename for the standalone config file (if specified). Default: `app`.
- `jupyterhub_app_venv`: String. Path to the JupyterHub instance's `venv`. Default: `/usr/local/jupyterhub`. You can set this to the value `system` to not use a virtual environment.
- `jupyterhub_app_config_dir`: String. Path to the JupyterHub's instance config dir. Default: `/usr/local/etc/jupyter`.
- `jupyterhub_app_pip`: String. Optional. Which package to install into the hub's venv (if set). Default: `""`.
- `jupyterhub_app_standalone_config`: String. Optional. [Trailets configuration for a standalone app](./jupyterhub_standalone_proxy.md#configuration-option-2). Default: `""`.
- `jupyterhub_app_pip_executable`: String. Which command to use to install packages into the venv (can be set to `uv` when it is available). Default: `pip`.

## Examples

See this role's molecule tests.

## See also

- Role [jupyterhub](./jupyterhub.md)
- Role [jupyterhub_standalone_proxy](./jupyterhub_standalone_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
