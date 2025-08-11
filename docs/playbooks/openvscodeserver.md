# Plabyook openvscodeserver
[back to index](../index.md#Roles)

## Summary

Installs [OpenVSCode Server](https://github.com/gitpod-io/openvscode-server), a webapplication that is a completely open source version of the server version of VSCode. Applying this role will provide the user with a fully functional web IDE running on the workspace, accessible through the browser at the workspace's FQDN (login via SRAM).

This component uses JupyterHub to spawn a separate instance of OpenVSCode Server for each user that logs in via the browser. This way, users do not have access to each other's data. The playbook can be added to a workspace that already contains a working JupterHub installation, or it can install JupyterHub itself (see the `openvscode_jupyter_force_install` parameter).

## Requires

* Debian-based system
* SRC Component: [SRC-Nginx Component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) must be executed prior to this component.
* *Optional*. A JupyterHub installation. Not necessary; the role can also install JupyterHub itself (see below).

## Variables

- `openvscode_base_path`: String. Base URI at which the app will be accessible. Default: `/`.
- `openvscode_jupyter_force_install`: Boolean. Install JupyterHub when it is not yet installed on the workspace. This will install JupyterHub in [standalone mode](../roles/jupyterhub_standalone_proxy.md), with OpenVSCode as a standalone application (without JupyterLab). You can add other components to the workspace that install different standalone apps (see [multiple apps](../roles/jupyterhub_standalone_proxy.md#hosting-multiple-standalone-apps)). Default: `true`.
- `openvscode_jupyter_config_dir`: String. Location of the directory containing the main JupyterHub config file. Default: `/usr/local/etc/jupyter`.
- `openvscode_jupyter_venv_path`: String. Location of the virtual environment in which JupyterHub is installed (or will be installed, if the force install param is set to true). Set to 'system' to not use a venv. Default: `/usr/local/jupyterhub`.


## See also

- role [openvscodeserver](../roles/openvscodeserver.md)
- role [jupyterhub_standalone_proxy](../roles/jupyterhub_standalone_proxy.md)
- role [jupyterhub_app](../roles/jupyterhub_app.md)
- role [nginx_reverse_proxy](../roles/nginx_reverse_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
