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

The periodic updates are enabled via a bootstrapping systemd timer: `upgrade-bootstrap.timer`. This timer ensures that there is a delay (see [Variables](#Variables) below) between the time the system boots, and the time the system starts checking for security updates. Without this delay, a security update might theoretically be triggered while Ansible is still working on executing components, which would lead to a dpkg conflict. `upgrade-bootstrap.timer` calls the `upgrade-bootstrap` service, which itself enables the standard Ubuntu unattended upgrade timers: `apt-daily.timer` and `apt-daily-upgrade.timer`. The bootstrap service also uninstalls itself, after the unattended upgrade timers have been activated.

The `update-bootstrap.timer` utilizes the `systemd` `Persistent=true` property to ensure that if a user stops the system before the set delay time, the timer is still triggered next time the system start.

The Ubuntu `apt-daily` and `apt-daily-upgrade` timers use the same mechanism, so if an update is scheduled at a time when the system is down, it will be scheduled when the system is next started up. *Note that there is a random delay between 0 and 60 minutes after boot before these timers are triggered*. So theoretically, starting a workspace for a short time (<60 minutes) and then restarting it again can mean that security updates are never triggered. As of Nov 2023, there is not way around this, save disabling the `RandomizedDelaySec` property of these timers. However, this is suboptimal: the random delay is in place to ensure that machines don't all connect to Ubuntu's apt repository simultaneously. `systemd` currently does not allow executing a timer immediately after boot *only* when a run was missed due to downtime, but with a random delay in all other cases.

## Variables

* `security_updates_firstrun`: Boolean (default: `true`). Whether to install available updates when the component is executed.
* `security_updates_periodic`: Boolean (default: `true`). Whether to enable periodic unattended upgrades.
* `security_updates_delay_time`: Integer (default: `30`). How many minutes after boot should periodic unattended upgrades be enabled? 

## History
2023 Written by Dawa Ometto (Utrecht University)


[back to index](../index.md#Roles)
