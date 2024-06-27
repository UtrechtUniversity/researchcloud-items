# Role sshfs-umount
[back to index](../index.md#Roles)

## Summary
Unmounts an earlier mounted filesystem.

## Requires
n/a

## Description
Unmounts an earlier mounted filesystem. For instance, this could be a filesystem mounted using
fuse mount over ssh.

The mountpoint must be provided as a Ansible parameter. Note that a prior invocation
of [sshfs-mount](sshfs-mount.md) in the same playbook is sufficient to 
set a value for this parameter, in that case no further action is required. 

## Variables
```yaml
sshfs_connection_info:
  mountpoint: "no default value!"
```

## See also
- [sshfs-mount](sshfs-mount.md)
- [sshfs-configrobot](sshfs-configrobot.md)
- [robotuser](robotuser.md)

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
