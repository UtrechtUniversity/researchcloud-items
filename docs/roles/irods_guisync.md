# Role irods_guisync  (deprecated)
[back to index](../index.md#Roles)

## Summary
NB: irods-guisync is deprecated, please use myrods_sync instead.

Installs desktop application to support data synchronization between a collection 
located on an iRODS server and a workspace folder. 

## Requires
Ubuntu desktop environment, iRODS icommands

## Description
The quisync function is a user-friendly version of the irsync command
found in the iRODS icommands set. The user can select a folder in
the workspace and a collection in the connected iRODS zone plus either
a retrieve or save action. The actual synchronization will be performed
through an irsync function of which the output is presented in a window.

Guisync assumes an initialized iRODS environment (configured connection).
A desktop launcher for the [iselect](irods_iselect.md) command is installed
as well, to help users initialize their iRODS environment from the desktop.

## Variables
```
irods_guisync_dir: "/usr/local/lib/irods_guisync"
```

## See also
[irods_icommands](irods_icommands.md)
[myrods_sync](myrods_sync.md)

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
