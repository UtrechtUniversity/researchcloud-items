# Role fact_workspace_info
[back to index](../index.md#Roles)

## Summary
Makes information about the workspace and CO available as Ansible facts. Provides three facts:

- `fact_workspace_info` -- Dict. Object containing info about the workspace (CO, user endpoint URL, etc.)/
- `fact_desktop_workspace` -- Boolean. True if the workspace has a desktop environment.
- `fact_workspace_storage` -- List. List of Strings of paths to ResearchCloud storage volumes mounted on the workspace.

## Requires
Linux flavor operating system.

## Description
See here for example output of the facts.

`fact_workspace_info`:

```json
"fact_workspace_info": {
    "co_admin_user_only": "false",
    "co_id": "coid",
    "co_name": "CO Name",
    "co_passwordless_sudo": "true",
    "co_roles_enabled": "true",
    "co_token": "token",
    "co_user_api_endpoint": "https://api.surfresearchcloud.nl/user/co_users/",
    "owner_id": "id",
    "workspace_id": "id2",
    "workspace_name": "python workbench3"
}
```

`fact_workspace_storage`: 

```json
 "fact_workspace_storage": [
    {
        "mount": "/data/foo",
        "device": "/dev/vdb1",
        "fstype": "xfs",
        "options": "rw,relatime,attr2,inode64,logbufs=8,logbsize=32k,noquota",
        "size_total": 53659811840,
        "size_available": 24005615616,
        "block_size": 4096,
        "block_total": 13100540,
        "block_available": 5860746,
        "block_used": 7239794,
        "inode_total": 26213824,
        "inode_available": 26196400,
        "inode_used": 17424,
        "uuid": "8a9dd671-1c48-4201-bc3h-350fcd883421"
    }
 ]
```

## History
2024 Written by Dawa Ometto (Utrecht University)



[back to index](../index.md#Roles)
