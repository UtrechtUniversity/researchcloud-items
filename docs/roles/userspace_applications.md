# Role userspace_applications
[back to index](../index.md#Roles)

## Summary
Scripts selected from the files contained in this role will be scheduled
to execute upon the first login of users, only once.  
This concept facilitates configuration done on
a per-user basis.

## Requires
Linux flavor operating system. Facilitates bash and zsh scripts.

## Description
Place your scripts in the `files` section of this role.
Then add this role to your playbook to have a selection of scripts added to
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
In the example, the scripts located in `userspace_applications/files` with the
names `10-python-poetry` and `999ready` are added to 
the runonce schedule.  Since `10-python-poetry` refers to a directory,
all the scripts held underneath that directory tree are included.
 
## Variables
The Ansible variable `list_userspace_applications` must be set by the calling 
playbook and should consist of a list of script filenames (see example above).

## See also
Role [userspace_applications](./userspace_applications.md) can be used to store
(sets of) your runonce scripts.

## History
2021 Written by Ton Smeele (Utrecht University)



[back to index](../index.md#Roles)
