# Role <name>
[back to index](../index.md#Roles)

## Summary
Clones a list of repositories into a directory.

## Requires
This role has no special requirements.

## Description
The purpose of this role is to facilitate end-users by already cloning one or more repositories. This role has the biggest for those who create environments for other users, where those users have limited knowledge of git but do need one/several repositories present on a system. It should only be used with such a scenario in mind.

## Variables
* repositories: A string of semi-colon (`;`) seperated URLs to git respositories (`HTTPS` format).
* git_dir: The directory to clone the repositories into. Defaults to `/git/var/`.

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Roles)
