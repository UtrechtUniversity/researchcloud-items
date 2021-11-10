# Role sshfs-configrobot
[back to index](../index.md#Roles)

## Summary
Registers Ansible variables in preparation of mounting a remote filesystem
over ssh protocol where the client authenticates as robotuser.

## Requires
Role [robotuser](robotuser.md) has been executed prior to invocation of this role.

## Description
An [sshfs-mount](sshfs-mount) requires scripts to specify parameters for connecting the client to a server, 
such as username, server address, and directory used as data source.
 
When a robotuser account is used for authentication with the server, we may opt to use default connection
parameters already known by the robotuser. 

This role can be used to load the default connection parameters held by the robotuser,
prior to requesting a remote filesystem mount. 
This circumvents the need to supply mount parameters explicitly in a plugin or playbook. 
The variables that will be set are: `sshfs_username`, `sshfs_server`, 
`sshfs_sourcepath`, `sshfs_mountpoint`.

## Variables
```
robotuser_name: "uurobot"
```

## See also
- [sshfs-mount](sshfs-mount.md)
- [sshfs-umount](sshfs-umount.md)
- [robotuser](robotuser.md)

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
