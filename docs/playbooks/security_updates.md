# Playbook shared_directories
[back to index](../index.md#Playbooks)

## Summary

Enables a number of measures to ensure the workspace receives security updates.

## Requires
Ubuntu operating system.

## Description

This component concerns Ubuntu's so-called [unattended upgrades feature](https://help.ubuntu.com/community/AutomaticSecurityUpdates). This feature installs *only* updates from Ubuntu's default security channel, which are therefore deemed critical and stable by Canonical. Without this component, an SRC workspace will **not** install security updates automatically.

Note that updates that need a reboot to become active will *not* trigger an automatic reboot (this is up to the user). However, it is still possible that when e.g. a webserver is updated through unattended upgrades, this results in downtime. Disabling periodic unattended upgrades is thus configurable by the user. **The user should decide whether the risk of service disruption outweighs the risks of an unupdated workspace.**

This component provides the following features:

1. Install the latest security updates at when the component is executed.
1. Start checking for and auto-installing new security updates after a certain time.

Which of the following features are enabled can be configured using variables.

## Variables

See the corresponding [role](../roles/security_updates.md) for documentation.

## See also

Role [security_updates](../roles/security_updates.md)

## History
2023 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Playbooks)
