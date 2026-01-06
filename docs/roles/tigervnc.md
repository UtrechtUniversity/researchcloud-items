# Role tigervnc
[back to index](../index.md#Roles)

## Summary
Installs [TigerVNC](https://tigervnc.org/) server.

## Requirements

- Debian/Ubuntu workspace with Desktop

## Description

Installs the required packages for TigerVNC.

TigerVNC is not automatically run: different roles or playbooks can determine when and how VNC sessions should be created. See e.g. the [JupyterHub playbook](../../playbooks/jupyterhub.yml).

The `tigervnc_xstartup_path` fact is set to the value of the default `xstartup` script installed by TigerVNC. This can be used to start VNC sessions.

## See also

- playbook [jupyterhub](../../playbooks/jupyterhub.yml)

## History
2022-24 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)