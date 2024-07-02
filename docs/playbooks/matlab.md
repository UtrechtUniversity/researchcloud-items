# Playbook matlab
[back to index](../index.md#Playbooks)

## Summary
Install products from the [Matlab](https://nl.mathworks.com/) data analysis suite.

## Requires

- Ubuntu with desktop.
- Requires the [robotuser](./robotuser.md) component to be executed before this one.


## Description

The selected Matlab products will be installed, but not activated.  Users that login to the
workspace desktop (GUI) use a desktop menu command to activate Matlab using their own 
Matlab license. After this one-time activation per user, Matlab can be used via the
graphical user interface or in a commandline shell.

NB: Per-user activation is not needed if a license server is configured.

## Variables

- `matlab_cleanup_robot`. Boolean. Required. Whether to remove the connection to the robot server and the robotuser after matlab has been installed (set to false if another component needs the connection after this one). Default: `true`.

Additionally, some Ansible variables *must* be customized, such as the product subset to be installed, and keys and files related to the products. 
See the [matlab](../roles/matlab.md) role for details on how to configure
the installation.

## See also
[matlab role](../roles/matlab.md)

## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
