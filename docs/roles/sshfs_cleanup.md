# Role sshfs_cleanup
[back to index](../index.md#Roles)

## Summary

Cleans up the filesysted mounted via [sshfs_mount](./sshfs_mount.md) and deletes the [robotuser](./robotuser.md). 

This role can be conditionally included by a component's playbook: if another component needs to use the connection to the robotserver, this role can be skipped, whereas when the component is the last to use the robotserver, the connection and robotuser can be removed. See e.g. the [matlab component](../playbooks/matlab.md#variables) for an example of a playbook that implements this logic.

## Requires

Requires the `sshfs_connection_info` variable to be set in another role ([sshfs_configrobot](./sshfs_configrobot.md)).

## Variables
```yaml
sshfs_connection_info:
  mountpoint: "no default value!"
```

## See also
- [sshfs_mount](sshfs_mount.md)
- [sshfs_configrobot](sshfs_configrobot.md)
- [robotuser](robotuser.md)

## History
2021-2024 Written by Ton Smeele and Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
