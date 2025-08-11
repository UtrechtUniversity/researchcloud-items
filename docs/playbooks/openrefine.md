# Playbook openrefine
[back to index](../index.md#Roles)

## Summary

This role installs [OpenRefine]https://openrefine.org/), an open-source web application for data cleanup and transformation to other formats, an activity commonly known as data wrangling.

This component uses JupyterHub to spawn a separate instance of OpenRefine for each user that logs in via the browser. This way, users do not have access to each other's data. The playbook can be added to a workspace that already contains a working JupterHub installation, or it can install JupyterHub itself (see the `openrefine_jupyter_force_install` parameter).

## Variables

- `openrefine_version`: String. Specific version which should be fetched. Should correspond to one of the version string from the [openrefine GitHub releases](https://github.com/OpenRefine/OpenRefine/releases/), e.g. `3.9.3`. Default: `""` (which means the latest version will be fetched).
- `openrefine_extensions`. Optional. String. A YAML-string of a list of dictionaries that specify extensions to be downloaded. See the [role documentation](../roles/openrefine.md) for the specification of the dictionaries.

Note: the [FilesExtension](https://github.com/OpenRefine/FilesExtension) extension (which allows the user to import data from the server's local filesystem) is already installed by default.

## See also

- Role [jupyterhub_standalone_proxy](./jupyterhub_standalone_proxy.md)
- Playbook [openrefine](../roles/openrefine.md)

## History
2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
