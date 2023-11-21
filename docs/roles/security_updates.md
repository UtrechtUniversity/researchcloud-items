# Role runonce
[back to index](../index.md#Roles)

## Summary

Enables a number of measures to ensure the workspace receives security updates. See the Playbook docs for background.

## Requires
Ubuntu operating system.

## Description

Unattended security updates are enabled by default on Ubuntu. However, on cloud VMs, this feature can cause issues with a dpkg lock conflict during provisioning. It is therefore currently disabled on SURF Research Cloud. This role works around this issue by providing the following features:

1. Install the latest security updates at execution-time.
  * Achieved by installing the `unattended-upgrades` package and running `unattended-upgrades` at execution time.
1. Start checking for and auto-installing new security updates after a certain time.
  * Achieved by installing a `systemd` service that bootstraps activation of the `apt-daily.timer` and `apt-daily-upgrades.timer` services afer a set delay (see [Variables](#Variables)). Note that this service (`upgrade-bootstrap.timer`) has the `Persistent=true` property, so that if the workspace is stopped before the set delay is reached, the bootstrap script will nonetheless execute when the workspace is started again.

## Variables

* `security_updates_firstrun`: Boolean (default: `true`), whether to install available updates when the component is executed.
* `security_updates_periodic`: Boolean (default: `true`), whether to enable periodic unattended upgrades.
* `security_updates_delay_time`: Integer (default: `1`). When `security_updates_periodic` is enabled, how many days to wait before enabling unattended upgrades?

## History
2023 Written by Dawa Ometto (Utrecht University)


[back to index](../index.md#Roles)
