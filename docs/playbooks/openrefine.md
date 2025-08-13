# Playbook openrefine
[back to index](../index.md#Roles)

## Summary

This role installs [OpenRefine]https://openrefine.org/), an open-source web application for data cleanup and transformation to other formats, an activity commonly known as data wrangling.

This component uses JupyterHub to spawn a separate instance of OpenRefine for each user that logs in via the browser. This way, users do not have access to each other's data. The playbook can be added to a workspace that already contains a working JupterHub installation, or it can install JupyterHub itself (see the `openrefine_jupyter_force_install` parameter).

### Security note

JupyterHub spawns servers (JupyterLab) running under the `uid` of the user logged in the browser. Authentication in the browser is handled by SRAM: after logging in, the name of the user is set by SRAM in the `REMOTE_USER` header, and this is passed along to JupyterHub.

At the moment OpenRefine listens on a TCP port. This means users with shell access (and JupyterLab provides a shell!) can easily bypass authentication by hitting the address on localhost on which another user's OpenRefine server is listening. **Do not provide shell access to untrusted users**.

## Variables

- `openrefine_jupyter_config_dir`: String. Location of the directory containing the main JupyterHub config file.
- `openrefine_jupyter_venv_path`: String. Location of the virtual environment in which JupyterHub is installed (or will be installed, if the force install param is set to true). Set to `system` to not use a venv.
- `openrefine_jupyter_force_install`: Boolean. Whether to force installation of JupyterHub. If true, will install this application in standalone mode.
- `openrefine_max_memory`: String. Max RAM allowed to an instance of the OpenRefine app (corresponds to the -m command line argument). E.g. `6000M`. If empty, this will be set to a percentage of available RAM by default.
- `openrefine_base_path`: String. URI at which OpenRefine is served. Default: `/`. 
- `openrefine_extra_extensions`. Optional. String. A YAML-string of a list of dictionaries that specify extensions to be downloaded. See the [role documentation](../roles/openrefine.md) for the specification of the dictionaries.

Note: the [FilesExtension](https://github.com/OpenRefine/FilesExtension) extension (which allows the user to import data from the server's local filesystem) is already installed by default.

## See also

- Role [jupyterhub_standalone_proxy](./jupyterhub_standalone_proxy.md)
- Playbook [openrefine](../roles/openrefine.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
