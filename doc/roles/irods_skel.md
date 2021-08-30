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

This role preconfigures the file `~/.irods/irods_environment.json` with default
values for those advanced settings.

Disclaimer: The default values instantiated by irods_skel may not be suitable for your zones.
Use the [iselect](./irods_iselect.md) role with a list of zones/properties to obtain a more reliable mechanism.
 
## Variables

## See also
- [irods_repo](./irods_repo.md)  
- [irods_icommands](./irods_icommands.md)  
- [irods_iselect](./irods_iselect.md)  

## History
2021 Written by Ton Smeele (Utrecht University)


[back to index](../index.md#Roles)
