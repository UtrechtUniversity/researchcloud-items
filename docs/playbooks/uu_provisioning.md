# Playbook uu_provisioning
[back to index](../index.md#Playbooks)

## Summary
This playbook provides a way to perform tasks that should be executed on all UU workspaces.

### Requirements
- Unix-like OS

## Description

- *Optional*. Installs the latest [security updates](../roles/security_updates.md) on workspace creation.
- Runs the [uu_generic role](../roles/uu_generic.md):
  * places documentation and contact links on the workspace
  * installs generic applications
- *Optional*. Allows group `src_co_admin` to use `sudo` without a password. This is to ensure that the Collaborative Organisation admin group can use sudo on the machine, allowing us to disable the ResearchCloud co_passwordless_sudo parameter, which grants passwordless sudo to *all* CO users on the machine.

## Variables

- `uu_provisioning_security`. Boolean. Whether to install automatic security updates on workspace creation. Default: `false` (this is currently already done by SURF components).
- `uu_provisioning_co_admin_sudo`. Boolean. Whether group `src_co_admin` should get passwordless `sudo` rights (see above).

## See also

- role [uu_generic](../roles/uu_generic.md)
- role [security_updates](../roles/security_updates.md)

## History
2024-2025 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
