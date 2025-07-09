# Playbook irods-desktop
[back to index](../index.md#Playbooks)

## Summary
Installs applications that support users to access 
an [iRODS](https://www.irods.org) server from the Linux graphical desktop menu. 

## Requires
Linux operating system flavor with desktop and major version as supported by iRODS.

Also requires that [iRODS icommands](icommands.md) are installed.

## Description
The playbook installs: 
- The Yoda data synchronization desktop application [myrods_sync](../roles/myrods_sync.md).
This application allows users to synchronize data stored in a collection
on an iRODS server with a workspace folder.
- A desktop launcher for [iselect](../roles/irods_iselect.md) to allow the user to
initialize/configure a connection to an iRODS server from the desktop.


## Variables
n/a

## See also
- Role [myrods_sync](../roles/myrods_sync.md)
- Role [irods_icommands](../roles/irods_icommands.md)  
- Role [irods_iselect](../roles/irods_iselect.md)
- Role [irods_repo](../roles/irods_repo.md)  
- Role [irods_skel](../roles/irods_skel.md)  


## History
2021 Written by Ton Smeele (Utrecht University)    
2022 Updated to install myrods_sync instead of irods-guisync

[back to index](../index.md#Playbooks)
