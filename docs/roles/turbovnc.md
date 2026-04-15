# Role turbovnc
[back to index](../index.md#Roles)

## Summary
Installs [TurboVNC](https://turbovnc.org/) server as well as the [VirtualGL](https://www.virtualgl.org/) library for hardware-accellerated rendering. TurboVNC is optimized for fast GPU accellerated rendering.

## Requirements

- Debian/Ubuntu workspace with Desktop

## Description

Installs the required packages for TurboVNC from the TurboVNC apt PPA.

TurboVNC is not automatically run: different roles or playbooks can determine when and how VNC sessions should be created. See e.g. the [JupyterHub playbook](../../playbooks/jupyterhub.yml).

The `vnc_xstartup_path` fact is set to the value of the default `xstartup` script installed by TurboVNC. This can be used to start VNC sessions.

## See also

- playbook [jupyterhub](../../playbooks/jupyterhub.yml)
- role [tigervnc](./tigervnc.md)

## History
2022-24 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)