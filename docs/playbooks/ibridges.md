# Playbook iBridges
[back to index](../index.md#Playbooks)

## Summary
Installs the [iBridges](https://github.com/UtrechtUniversity/iBridges) pip library and command line tool 
for all users. After installation, the command `ibridges` is available for all users with a login shell.

## Requires

- Linux operating system
- pip

## Description

The playbook:

* installs the latest iBridges version from pip, in a common location for all users (see the `pip_install_systemwide` role).
* adds this common location to `$PYTHONPATH` for all users
* adds the iBridges command line utility to each user's `$PATH`

## Variables
See [irods_iselect](../roles/irods_iselect.md) for options to configure a list of zones.

## See also
- Role [pip_install_systemwide](../roles/pip_install_systemwide.md)


## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
