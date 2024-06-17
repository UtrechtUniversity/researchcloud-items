# Role fact_workspace_info
[back to index](../index.md#Roles)

## Summary
Makes information about the workspace and CO available as Ansible facts. Provides three facts:

- `fact_workspace_info` -- dict object containing info about the workspace (CO, user endpoint URL, etc.)/
- `fact_desktop_workspace` -- Boolean, true if the workspace has a desktop environment.

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

## History
2024 Written by Dawa Ometto (Utrecht University)



[back to index](../index.md#Roles)
