# Playbook miniconda
[back to index](../index.md#Playbooks)

## Summary
Installs a Python development environment equiped with *[miniconda](https://docs.conda.io/en/latest/miniconda.html)* for environment and module dependency management.

## Requires
Unix-environment.

## Description
Miniconda can be installed either for each user individually, or once and be shared amongst all users. 
Both options cannot be selected simultaneously.
By default it is installed systemwide. If the option to install for all users is selected, it will be installed at the first login of each user.
It follows the official documentation's recommended way of installation.
When it is installed, allows users to share both a list of environments and their packages.
Possible to-do would be to toggle whether user share packages amongst each other.

## Variables
- `miniconda_userspace:`: Boolean determining whether each user should gets their own installation. Default: true
- `miniconda_userspace_preinstall`: Boolean determining whether miniconda should be installed for each user when the component is executed, **so before the user first logs in**. Default: false.
- `miniconda_systemwide`: Boolean determining whether all users share one installation. Default: false
- `miniconda_auto_init`: Boolean determining whether `conda init` should be run automatically for each user. Useful if you do no want users' shells on the workspace to use conda's version of python by default. Default: true. If set to false, `<condadir>/condabin` will still be added to users' path, so they can run `conda init` manually.
- `miniconda_download_dest`: Directory to store the download files. Default: /usr/local/miniconda
- `miniconda_install_dir`: Directory to install the shared system-wide installation, if selected. Default: /opt/miniconda
- `miniconda_url`: URL to download miniconda from. Default: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

## See also
- role [fact_regular_users](../roles/fact_regular_users.md)
- role [runonce](../roles/runonce.md)

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Playbooks)
