# Role fact_workspace_info
[back to index](../index.md#Roles)

## Summary
Makes information about the workspace and CO available as Ansible facts. Provides three facts:

- `fact_workspace_info` -- dict object containing info about the workspace (CO, user endpoint URL, etc.)/
- `fact_co_users` -- list of dict objects representing the SRAM users on the workspace.
- `fact_co_groups` -- dict with group names from the CO as keys, and lists of usernames in those groups as values. 

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

`fact_co_users`:

```json
"fact_co_users": [
    {
        "integer_id": 1781,
        "research_drive_secret": null,
        "roles": [
            "rsc_developers",
            "src_developers",
            "@all",
            "src_co_developer"
        ],
        "services": [],
        "ssh_keys": [
            "ssh-rsa bla"
        ],
        "username": "foo"
    }
]
```

`fact_co_groups`:

```json
"fact_co_groups": {
    "@all": [
        "user1",
        "user2"
    ],
    "rsc_developers": [
        "user1",
        "user2"
    ],
    "src_co_admin": [
        "user1",
        "user2"
    ],
    "src_co_developer": [
        "user1",
        "user2"
    ],
    "src_co_wallet": [
        "user1",
        "user2"
    ],
    "src_developers": [
        "user1",
        "user2"
    ],
    "src_ws_admin": [
        "user1",
        "user2"
    ]
}
```


## History
2024 Written by Dawa Ometto (Utrecht University)



[back to index](../index.md#Roles)
