# Role fact_regular_users
[back to index](../index.md#Roles)

## Summary
Makes information available about regular users (excluding system process users) and groups.

Defines the following two facts:

- `fact_regular_users` -- list of dicts containing user info about regular users.
- `fact_co_groups` -- dict with group names from the CO as keys, and lists of usernames in those groups as values. 

## Requires
Linux flavor operating system.

## Description
The role sets the Ansible variable `fact_regular_users` to a list of users. Information from /etc/cpasswd is filtered on: 1) userid >= 1000 and  2) user has a home directory located underneath /home/

The fact `fact_co_groups` is filled with the members of the unix groups listed in `/etc/rsc/managedgroups`, which are the groups corresponding to roles defined for the CO in SRAM.

## Variables
The variable `fact_regular_users` and `fact_co_groups` are filled. Examples:

`fact_regular_users`:

```yaml
[
  {
    user: "foo", 
    userid: 1000, 
    groupid: 1000, 
    home: "/home/foo", 
    shell: "/bin/bash",
    description: "sample user foo"
  }  
]
```

`fact_co_groups`:

```yaml
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

## See also

Role [runonce](./runonce.md).


## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
