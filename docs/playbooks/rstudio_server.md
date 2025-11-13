# Playbook RStudio Server
[back to index](../index.md#Roles)

## Summary

This role installs [RStudio Server](https://posit.co/products/open-source/rstudio/), an open-source IDE for R programming. It integrates RStudio Server within a JupyterHub environment, enabling users to access the IDE via their browsers. Login via SRAM.

The playbook supports two modes of operation:
1. **Standalone mode**: RStudio Server runs independently of JupyterLab. Users are immediately directed to RStudio.
2. **Non-standalone mode**: RStudio Server is configured as a JupyterLab extension and can be launched by users within the JupyterLab interface, which they see when they login to the wroskpace. This mode integrates RStudio seamlessly into a multi-application JupyterHub setup.

### Security note

In both modes, RStudio Server instances are spawned by JupyterHub and run under the user’s credentials. Each user has an isolated instance, ensuring data separation. RStudio is run using a Unix Domain Socket, ensuring that users with shell access cannot directly connect to another user's server.

## Variables

- `rstudio_fqdn`: String. Fully Qualified Domain Name (FQDN) where RStudio Server/JupyterHub will be served. Defaults to `localhost`.
- `rstudio_base_path`: String. URI at which RStudio Server is served. Default: `/`.
- `rstudio_jupyter_venv_path`: String. Location of the virtual environment for JupyterHub and related components. Default: `/usr/local/jupyterhub`.
- `rstudio_standalone`: Boolean. Specifies whether RStudio Server should be installed in standalone mode. Default: `false`.
- `rstudio_pip_cmd`: String. Command used to install pip packages (default: `uv`, can be set to `pip`).

## See also

- Role [rstudio](../roles/rstudio.md)
- Role [jupyterhub_standalone_proxy](../roles/jupyterhub_standalone_proxy.md)
- Role [jupyterhub_app](../roles/jupyterhub_app.md)

## History
2026 Written by Dawa Ometto (Utrecht University).

[back to index](../index.md#Roles)