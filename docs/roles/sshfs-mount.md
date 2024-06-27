# Role sshfs-mount
[back to index](../index.md#Roles)

## Summary
Performs a fuse-mount of a filesystem using ssh protocol.

## Requires
n/a

## Description
Using sshfs, workspace users can mount a remote filesystem over ssh protocol. 
This role performs the equivalent of an `sshfs <username>@<server>:/<sourcepath> <mountpoint>` Linux
command, using key-based authentication.

## Variables
```yaml
sshfs_connection_info:
  username: "SSHFS_USERNAME_MISSING"
  server: "SSHFS_SERVER_MISSING"
  port: "22"
  sourcepath: "SSHFS_SOURCEPATH_MISSING"
  mountpoint: "SSHFS_MOUNTPOINT_MISSING"
```

## See also
- [sshfs-umount](sshfs-umount.md)
- [sshfs-configrobot](sshfs-configrobot.md)
- [robotuser](robotuser.md)

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
