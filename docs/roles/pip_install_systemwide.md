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
- `custom_pip_path_profile`: String. Name of the script to be placed in `/etc/profile.d` updating the user's path. Default: `uu-custom-pip.sh`.

Note that if you first use this role to install something to `/usr/local/pip`, and then again to install something else to `/var/pip`, this would cause the default `custom_pip_path_profile` (`/etc/profile.d/uu-custom-pip.sh`) to be overwritten, so that only `/var/pip` will be on the path. To remedy this, be sure to specify a custom `custom_pip_path_profile` when you use a `custom_pip_path` other than the default.

## See also

- [Role pip](pip.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
