# Playbook icommands
[back to index](../index.md#Playbooks)

## Summary
Installs the icommands client tools (and iselect) that facilitate users to access 
an [iRODS](https://www.irods.org) server from within a shell. 

## Requires
Linux operating system flavor as supported by iRODS.

## Description
The playbook installs the latest icommands client and iRODS runtime libraries
from the iRODS repository.
Furthermore, the tool `iselect` is installed which can be used to connect to
some preconfigured iRODS zones.

## Variables
See [irods_iselect](../roles/irods_iselect.md) for options to configure a list of zones.

## See also
- Role [irods_icommands](../roles/irods_icommands.md)  
- Role [irods_iselect](../roles/irods_iselect.md)
- Role [irods_repo](../roles/irods_repo.md)  
- Role [irods_skel](../roles/irods_skel.md)  


## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
