# Playbook robotuser
[back to index](../index.md#Playbooks)

## Summary
Installs a Linux robot user. When the workspace desires
to use a remote service then the robot user can be used to authenticate.

## Requires
n/a

## Description
Installs a robot user on a workspace to allow the workspace to authenticate
with a (robot) server. 

## Variables
```
robotuser_key:  # no default!   - private key for robot user
robotuser_server: # no default!   - robot server ip address
robotuser_sourcepath: # no default! - path to served files e.g. /data/volume_2
```
The above variables must be supplied as parameter to the playbook.

## See also
[sshfs-configrobot](../roles/sshfs-configrobot) robot used to mount remote filesystem

## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
