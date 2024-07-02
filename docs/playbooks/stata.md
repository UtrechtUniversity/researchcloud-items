# Playbook stata
[back to index](../index.md#Playbooks)

## Summary
Install [Stata 18](https://www.stata.com/).

## Requires

- Ubuntu with desktop.
- Requires the [robotuser](./robotuser.md) component to be executed before this one.

## Variables

- `stata18_cleanup_robot`. Boolean. Required. Whether to remove the connection to the robot server and the robotuser after stata has been installed (set to false if another component needs the connection after this one). Default: `true`.

The following variables are Strings required to activate the license:

- `stata18_lic_auth`
- `stata18_lic_code`
- `stata18_lic_name`
- `stata18_lic_org`
- `stata18_lic_serial`

## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
