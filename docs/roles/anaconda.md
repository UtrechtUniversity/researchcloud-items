# Role anaconda
[back to index](../index.md#Roles)

## Summary
Role that install Anaconda, a distribution of Python and R for Data Science. See the [Anaconda website](https://www.anaconda.com/) for more details.

## Requires
Debain or RHEL/CentOS.

## Description
The role follows the installation as explained on their official website. It install any required dependencies and then Anaconda itself. The installation is done in a shared location and each user on the system is granted access rights to all necessary files.

## Variables
* `anaconda_python_version`: The Python version to use for the Anaconda installation. Default: `3`.
* `anaconda_version`: The Anaconda version that will be installed. See https://docs.anaconda.com/anaconda/reference/release-notes/. Default: `2022.05`.
* `anaconda_ip`: The address to reach Anaconda. Default: `0.0.0.0`.
* `anaconda_port`: Which port to assign to Anaconda. Default: `8888`.
* `anaconda_download_dest`: Where to download the installation file to. Defualt: `/tmp/anaconda3`.
* `anaconda_install_dir`: Where to install Anaconda. Default: `/opt/anaconda3`.

## See also
[fact_regular_users](fact_regular_users.md)
[runonce](runonce.md)
[desktop_file](desktop_file.md)

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Roles)
