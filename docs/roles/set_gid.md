# Role runonce
[back to index](../index.md#Roles)

## Summary

Ensures certain directories are owned by a specified group and have `setgid` enabled ([setgid explanation](https://linuxconfig.org/how-to-use-special-permissions-the-setuid-setgid-and-sticky-bits)). 

## Requires
Linux flavor operating system.

## Description

## Variables

* `set_gid_groupname`: the name of the group to make the owner of the directories
* `set_gid_paths`: comma-separated list of paths to directories to chown and enable setgid on

## History
2023 Written by Dawa Ometto (Utrecht University)



[back to index](../index.md#Roles)
