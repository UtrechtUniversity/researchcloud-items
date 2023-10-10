# Role runonce
[back to index](../index.md#Roles)

## Summary

Creates a default group for all users of a workspace. Creates the group, add all [regular users](../roles/fact_regular_users.md) to it, and ensures that new users are also added to it.

## Requires
Debian/Ubuntu operating system.

## Description

1. Adds the group with the desired name and gid.
1. Modifies `/etc/security/group.conf` so that the group is added by PAM whenever a user logs in.
1. Takes all existing regular users and adds them to group.
1. Adds the group to the `EXTRA_GROUPS` instruction in `/etc/adduser.conf` so that new users created with `/sbin/adduser` (a Debian/Ubuntu tool, not to be confused with `useradd`) are automatically added to the new group.
  * also ensures that existing groups in `EXTRA_GROUPS` are kept. On SRC workspaces, this includes the `davfs2` group by default.
 
## Variables

* dict `default_group_group`:
  * `default_group_group.groupname`: name of the group to create
  * `default_group_group.gid``: # optional. gid (numeric) of the group

## See also

## History
2023 Written by Dawa Ometto (Utrecht University)



[back to index](../index.md#Roles)
