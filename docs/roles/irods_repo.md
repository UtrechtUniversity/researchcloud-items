# Role irods_repo
[back to index](../index.md#Roles)

## Summary
Adds the iRODS repository as a source of software packages. 

## Requires
Linux distribution that supports either yum or apt package manager

## Description
The RENCI iRODS repository is added as a source. An alternative
source repo (e.g. experimental builds) can be specified in an Ansible variable.
See related roles to install software packages.

## Variables
The following variables and defaults are available:
```
irods_repo_yum_major_version: "{{ ansible_distribution_major_version }}"
irods_repo_apt_release: "{{ ansible_distribution_release }}"
irods_repo_url: "https://packages.irods.org"
```

## See also
- [irods_icommands](./irods_icommands.md)  
- [irods_iselect](./irods_iselect.md)  
- [irods_skel](./irods_skel.md)

## History
2021 Written by Ton Smeele (Utrecht University)


[back to index](../index.md#Roles)
