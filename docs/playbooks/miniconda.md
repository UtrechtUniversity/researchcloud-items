# Playbook miniconda
[back to index](../index.md#Playbooks)

## Summary
Installs *[miniconda](https://docs.conda.io/en/latest/miniconda.html)* for environment and module dependency management.

## Requires
Unix-environment.

## Description
Miniconda is installed systemwide, with both the `conda` binary and a global package cache and environment directory in `/opt/miniconda`. `conda` is added to the path for all users.

Users can use either these global packages and environments, or create their own environments in their homedirecotires (in which case packages for those environments will also be installed in the homedirectory, i.e. in `~/.conda/pkgs`).

## Variables
- `miniconda_shared_editable`: Boolean determining whether the global system environments and pacakges should be writeable by all users.
- `miniconda_auto_init`: Boolean determining whether `conda init` should be run automatically for each user.
- `miniconda_download_dest`: Directory to store the download files. Default: `/usr/local/miniconda`.
- `miniconda_install_dir`: Directory to install the shared system-wide installation, if selected. Default: `/opt/miniconda`.
- `miniconda_url`: URL to download miniconda from. Default: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

## See also
- role [fact_regular_users](../roles/fact_regular_users.md)
- role [miniconda](../roles/miniconda.md)
- role [runonce](../roles/runonce.md)

## History
2022 Written by Sytse Groenwold, 2025 Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
