# Role pipx_install_systemwide
[back to index](../index.md#Roles)

## Summary

Installs python-based applications to a common location that can be used by all users on a machine, using [pipx](https://pipx.pypa.io/stable/). **An ordinary `pip install` as user `root` is not recommended, as it may interfere with `pip` packages installed by the system package manager (e.g. `apt`). So instead, use this role** to install applications to `/usr/local/uu-pip` (by default).

Note: `pipx` should only be used to install (GUI or command line) applications, not libraries!

## Requires

* Debian-based system
* RHEL-based system

## Description
This role:

- will install your desired pip packages to `/usr/local/uu-pip` (default).
- will add `/usr/local/uu-pip` to each user's `$PYTHONPATH` (by placing a script in `/etc/profile.d/`).
- will add `/usr/local/uu-pip/bin` to each user's `$PATH` (by placing a script in `/etc/profile.d/`).

## Variables

- `pipx_install_systemwide_packages`: List or String. Required. List or String of packages to install. For example: `['ibridges', 'foo']` or `ibridges`.
- `pipx_install_systemwide_executable`: String. Path to the Python executable to use for installing. Default: omitted.
- `pipx_install_systemwide_location`: String. Default: `/usr/local/pip`.
- `pipx_install_systemwide_profile`: String. Name of the script to be placed in `/etc/profile.d` updating the user's path. Default: `uu-custom-pip.sh`. Will not be created when empty.
- `pipx_install_systemwide_python`: String. Optinal. Path to the location of a python interpreter to be used for installing the app.
- `pipx_install_systemwide_use_uv`: Boolean. Optional. Set to true to use `uv tool` instead of `pipx` to install (`uv` is faster). Default: `false`.
- `pipx_install_systemwide_cmd`: String. Command to use for installation. Defaults to `pipx install` or `uv tool install` (when `pipx_install_systemwide_use_uv` is set to `true`).
- `pipx_install_systemwide_requirements`: String. Optional. Path to a requirements file to use for install dependencies for the specified packages. **Only usable when setting `pipx_install_systemwide_use_uv` to `true`**.

Note that if you first use this role to install something to `/usr/local/uu-pip`, and then again to install something else to `/var/pip`, this would cause the default `pipx_install_systemwide_location` (`/etc/profile.d/uu-custom-pip.sh`) to be overwritten, so that only `/var/pip` will be on the path. To remedy this, be sure to specify a custom `pipx_install_systemwide_profile` when you use a `pipx_install_systemwide_location` other than the default.

## See also

- [Role pip](pip.md)

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
