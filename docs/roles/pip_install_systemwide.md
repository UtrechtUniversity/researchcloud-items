# Role pip_install_systemwide
[back to index](../index.md#Roles)

## Summary

Installs `pip` packages to a common location so that the can be used by all users on a machine. **An ordinary `pip install` as user `root` is not recommended, as it may interfere with `pip` packages installed by the system package manager (e.g. `apt`). So instead, use this role** to install packages to `/usr/local/pip` (by default).

## Requires

* Debian-based system
* RHEL-based system

## Description
This role:

- will install your desired pip packages to `/usr/local/pip` (default).
- will add `/usr/local/pip` to each user's `$PYTHONPATH` (by placing a script in `/etc/profile.d/`).
- will add `/usr/local/pip/bin` to each user's `$PATH` (by placing a script in `/etc/profile.d/`).

## Variables

- `pip_install_systemwide_packages`: List or String. Required. List or String of packages to install. For example: `['ibridges', 'foo']` or `ibridges`.
- `custom_pip_path`: String. Default: `/usr/local/pip`.

## See also

- [Role pip](pip.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
