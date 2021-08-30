# Role irods_skel
[back to index](../index.md#Roles)

## Summary
Preconfigures an irods_enviromnent for new Linux users.
 

## Requires
Linux distribution

## Description
The iRODS icommand toolset allows Linux users to access an iRODS zone
via shell compatible commands. Its `iinit` command is used to set connectivity
parameters to access an iRODS zone. However, zones may require PAM based access
and encrypted connections that require more advanced settings to be configured.

This role preconfigures the `~/.irods/irods_environment.json` with common defaults
for those advanced settings.

Please see the [iselect](./irods_iselect) role for an alternative (or additional)
mechanism to select an iRODS zone from a distinct list.   

## Variables

## See also
- [irods_repo](./irods_repo)  
- [irods_icommands](./irods_icommands)  
- [irods_iselect](./irods_iselect)  

## History
2021 Written by Ton Smeele (Utrecht University)


[back to index](../index.md#Roles)
