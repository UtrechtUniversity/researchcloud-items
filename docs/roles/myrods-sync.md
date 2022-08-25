# Role myrods-sync
[back to index](../index.md#Roles)

## Summary
Installs desktop application to support data synchronization between a collection 
located on an iRODS server and a workspace folder. 

## Requires
Ubuntu desktop environment, iRODS icommands

## Description
The myrods-sync function is a user-friendly version of the irsync command
found in the iRODS icommands set. The user can select a folder in
the workspace and a collection in the connected iRODS zone plus either
a retrieve or save action. The actual synchronization will be performed
through an irsync function of which the output is presented in a window.

Myrods-sync will reuse an already initialized iRODS environment (configured connection)
and alternatively create one.

## Variables
```
myrodssync_git: "https://github.com/utrechtuniversity/myrods-sync.git"
myrodssync_dir: "/usr/local/lib/myrods-sync"
```

## See also
[irods_icommands](irods_icommands.md)

## History
2021 Written by Ton Smeele (Utrecht University)
2022 Renamed from guisync to myrods-sync, added iRODS environment initialization


[back to index](../index.md#Roles)
