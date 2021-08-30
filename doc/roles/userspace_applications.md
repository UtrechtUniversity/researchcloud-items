# Role <name>
[back to index](../index.md#Roles)

## Summary
Scripts selected from the files contained in this role will be scheduled
to execute upon the first login of users, only once.  
This concept facilitates configuration done on
a per-user basis.

## Requires
Linux flavor operating system. Facilitates bash and zsh scripts.

## Description
Add this role to your playbook to have a selection of scripts added to
a [runonce](./runonce.md) schedule.

Example of inclusion in a playbook: 
```
    roles:
      - role: userspace_applications
        vars:
          - list_userspace_applications:
            - "10-python-poetry"
            - "999ready"

```
The scripts located in `userspace_applications/files` with directory
named `10-python-poetry` and file named `999ready` will be added to 
the runonce schedule.  If the name refers to a directory
then all scripts held underneath that directory tree are included.
 
## Variables
The Ansible variable `list_userspace_applications` must be set by the calling 
playbook and consist of a list of script filenames (see example above).

## See also
Role [userspace_applications](./userspace_applications.md) can be used to store
(sets of) your runonce scripts.

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
