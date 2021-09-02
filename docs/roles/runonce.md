# Role runonce
[back to index](../index.md#Roles)

## Summary
Schedules so called "userspace application" scripts to run once (by each user), 
upon first login of the user.

## Requires
Linux flavor operating system. Facilitates bash and zsh scripts.

## Description
Bash/zsh scripts that need to run can be placed in directory `/etc/runonce.d`,
either directly or within a subdirectory. Upon the user's first login, 
the scripts will be run (only once) in sequence, sorted alphabetically by pathname.

Script(s) output (`stdout` and `stderr`) is saved in a file `~/.runonce.log`.

Note that the scripts are *sourced* by the login shell. This allows shell variables
to be set and used by subsequent scripts/interactions.

NB: In general, we recommend that you do *not* add this role to your playbook. 
Instead, please consider to store your scripts in role 
[userspace_applications](./userspace_applications.md) 
and add that role to your playbook. 
 
## Variables

## See also
Role [userspace_applications](./userspace_applications.md) can be used to store
(sets of) your runonce scripts.

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
