# Role runonce
[back to index](../index.md#Roles)

## Summary

Adds packages to predefined Aptly repositories. Used in combination with the [aptly component](../playbooks/aptly.md).

## Requires

Debian/Ubuntu operating system.

## Description

1. Adds a script `/usr/local/bin/aptly_add_packages.sh` that adds packages from the [configured directories](../playbooks/aptly.md#aptly-packages) to the [configured Aptly repositories](../playbooks/aptly.md#aptly-repositories).
2. Triggers this script for a first run.
3. Ensures all files added to the repository in this way are readable by the webserver.
 
The `aptly_add_packages.sh` performs an `su` to the Aptly user, so it must be run by a user with appropriate privileges.

## Variables

All these variables are required:

- `aptly__packages`: See [aptly component](../playbooks/aptly.md#aptly-packages).
- `webserver_group`: String group of the webserver to be used to ensure readability of packages added to the repo.
- `aptly__user`: String name of the Aptly user.
- `aptly__homedir`: String homedirectory of the Aptly user.

## See also

## History
2023 Written by Dawa Ometto (Utrecht University)


[back to index](../index.md#Roles)
