# Playbook iBridges
[back to index](../index.md#Playbooks)

## Summary
Installs [iBridges](https://github.com/UtrechtUniversity/iBridges), the userfriendly client for iRODS (and Yoda). Installs the command line client, and also the GUI application on desktop workspaces. After installation, the command `ibridges` is available for all users with a login shell.

## Requires

- Linux operating system

## Description

The playbook:

* installs the latest iBridges version from pip, in a common location for all users (see the `pipx_install_systemwide` role).
* adds this common location to `$PYTHONPATH` for all users
* adds the iBridges command line utility to each user's `$PATH`
* on Desktop workspaces, installs the GUI application as well (Desktop item is places in the applications menu and on the desktop).

## See also
- Role [ibridges](../roles/ibridges.md)
- Role [pipx_install_systemwide](../roles/pipx_install_systemwide.md)
- Playbook [irods_tools](./irods_tools.md)


## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
