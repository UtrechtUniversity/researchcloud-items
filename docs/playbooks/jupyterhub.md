# Plabyook jupyterhub
[back to index](../index.md#Roles)

## Summary

Installs [JupyterHub](https://jupyterhub.readthedocs.io/), with SRAM login.

Although SURF also has a *Jupyter Notebooks* component that installs JupyterHub, this component was created to provide some extra features:

- Install JupyterHub in a virtual environment instead of using the system's python packages
- Extra security features (WIP, see [below](#security-note))
- Configure the Hub to be able to add arbitrary extensions to JupyterLab, or arbritary standalone apps to the Hub, using other components.
    - See the [jupyterhub_app role](../roles/jupyterhub_app.md) for this.

## Requires

* Debian-based system
* SRC Component: [SRC-Nginx Component](https://gitlab.com/rsc-surf-nl/plugins/plugin-nginx) must be executed prior to this component.

## Description

The role:

- Creates a reverse proxy to serve JupyterHub
- Installs JupyterHub into a virtual environment
- Configures JupyterHub to support login via SRAM
- Creates a systemd service for JupyterHub

### Security note

JupyterHub spawns servers (JupyterLab) running under the `uid` of the user logged in the browser. Authentication in the browser is handled by SRAM: after logging in, the name of the user is set by SRAM in the `REMOTE_USER` header, and this is passed along to JupyterHub. At the moment JupyterHub listens on a TCP port (8000). This means users with shell access (and JupyterLab provides a shell!) can easily bypass authentication by hitting `localhost:8000/user/arbitraryusername` -- this will spawn a Lab instance running as user `arbitraryusername`. **Do not provide shell access to untrusted users**.

Work is in progress to remedy this issue by letting JupyterHub listen on unix sockets.

This component (unlike SURF's Jupyter Notebooks component) does configure JupyterLab to use unix sockets to spawn user's [Jupyter kernels](https://docs.jupyter.org/en/stable/projects/kernels.html).

## Variables

The following parameters are supported:

- `jupyter_uri`
- `jupyter_extra_pkgs`
- `jupyter_config_extra`

They correspond to the equivalent variables documented for the [jupyterhub role](../roles/jupyterhub.md#variables) 

## See also

- role [jupyterhub](../roles/jupyterhub.md)
- role [nginx_reverse_proxy](../roles/nginx_reverse_proxy.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
