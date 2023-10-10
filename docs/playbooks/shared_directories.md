# Playbook shared_directories
[back to index](../index.md#Playbooks)

## Summary

Creates directories on the workspace for collaboration between different users.

## Requires
Linux operating system

## Description

Workspaces come with a `/scratch` directory meant for collaboration between users. However, files created in this directory are by default still owned by the `uid` and `gid` of the user who creates them. This means that these files cannot by default by edited by other users. This component addresses this issue by:

1. creating a group (default name: `sharing`) to which all [regular users](../roles/fact_regular_users.md) belong
1. setting `setgid` on desired directories, so that files created in these directories have the `sharing` group as group owner

## Variables

* `group_name`: name of the group to be created (default: `sharing`).
* `paths`: comma-separated paths to the directories which should receive `set_gid` (default: `/shared`).

## See also

Role [default_group](../roles/default_group.md)
Role [set_gid](../roles/set_gid.md)

## History
2023 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
